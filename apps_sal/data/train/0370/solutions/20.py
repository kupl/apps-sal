class Solution:
    def get_prime_numbers(self, num_to_idx_dict, max_num: int) -> List[int]:
        is_prime_list = [True] * (max_num + 1)
        prime_to_nums_dict = defaultdict(list)

        for i in range(2, max_num // 2 + 1):
            if is_prime_list[i] == False:
                continue
            num = i
            while num <= max_num:
                if num in num_to_idx_dict:
                    prime_to_nums_dict[i].append(num_to_idx_dict[num])
                is_prime_list[num], num = False, num + i

        return prime_to_nums_dict

    def find(self, union_list, index: int) -> int:
        if index == union_list[index]:
            return index
        parent = self.find(union_list, union_list[index])
        union_list[index] = parent
        return parent

    def union(self, union_list, index1: int, index2: int) -> None:
        union1, union2 = self.find(union_list, index1), self.find(union_list, index2)
        union_list[index2] = union2
        union_list[union1] = union2

    def largestComponentSize(self, A: List[int]) -> int:
        if len(A) == 0:
            return 0
        max_num = max(A)
        union_list, count_list = [i for i in range(len(A))], [0] * (len(A))
        num_to_idx_dict = dict(list(zip(A, list(range(len(A))))))

        # get prime numbers
        prime_to_nums_dict = self.get_prime_numbers(num_to_idx_dict, max_num)  # prime numbers of A's numbers

        # linking numbers having the same prime
        for prime, nums in list(prime_to_nums_dict.items()):
            for i in range(len(nums) - 1):
                self.union(union_list, nums[i + 1], nums[i])

        # counting numbers in a component
        for i, num in enumerate(A):
            count_list[self.find(union_list, i)] += 1

        return max(count_list)
# Time complexity: O(n * p) where n is the maximum number of A and p is the number of prime numbers less than n
# Space complexity: O(n + p) we can ignore p
