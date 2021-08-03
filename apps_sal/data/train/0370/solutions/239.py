class Solution:
    def get_prime_numbers(self, A, max_num: int) -> List[int]:
        is_prime_list = [True] * (max_num + 1)
        prime_to_nums_dict = defaultdict(list)

        for i in range(2, max_num + 1):
            if is_prime_list[i] == False:
                continue

            num = i
            while num <= max_num:
                if num in A:
                    prime_to_nums_dict[i].append(num)
                is_prime_list[num] = False
                num += i

        return prime_to_nums_dict

    def find(self, union_list, index: int) -> int:
        if index == union_list[index]:
            return index
        # return self.find(union_list, union_list[index])
        parent = self.find(union_list, union_list[index])
        union_list[index] = parent
        return parent

    def union(self, union_list, index1: int, index2: int) -> None:
        union1, union2 = self.find(union_list, index1), self.find(union_list, index2)
        union_list[union1], union_list[index2] = union2, union2
        #union_list[union1] = union2

    def largestComponentSize(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        max_num = max(A)
        union_list = [i for i in range(max_num + 1)]
        count_list = [0] * (max_num + 1)

        # get prime numbers
        prime_to_nums_dict = self.get_prime_numbers(set(A), max_num)  # prime numbers of A's numbers

        # linking numbers having the same prime
        for prime, nums in list(prime_to_nums_dict.items()):
            for i in range(len(nums) - 1):
                self.union(union_list, nums[i], nums[i + 1])

        # print(prime_to_nums_dict)
        # print(union_list)

        # counting numbers in a component
        for i, num in enumerate(A):
            # if num == 1: continue
            count_list[self.find(union_list, num)] += 1
        # print(count_list)
        return max(count_list)
# Time complexity: O(n * p) where n is the maximum number of A and p is the number of prime numbers less than n
# Space complexity: O(n + p) we can ignore p
