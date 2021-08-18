class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cost = 0
        max_nb_op_1 = 0
        for i in range(len(nums)):
            nb_op_0 = nb_op_1 = 0
            x = nums[i]
            while x > 0:
                if x % 2 != 0:
                    nb_op_0 += x % 2
                    x -= x % 2
                if x > 0:
                    nb_op_1 += 1
                    x = x // 2
            cost += nb_op_0
            max_nb_op_1 = max(max_nb_op_1, nb_op_1)
        cost += max_nb_op_1
        return cost

    def minOperations_dumb_solution(self, nums: List[int]) -> int:
        cost = 0
        while True:
            all_zeros = True
            all_evens = True
            for i in range(len(nums)):
                if nums[i] == 0:
                    continue

                all_zeros = False
                if nums[i] % 2 != 0:
                    cost += nums[i] % 2
                    nums[i] = nums[i] - (nums[i] % 2)
                    all_evens = False

            if all_zeros:
                break
            while all_evens:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                    if nums[i] % 2 != 0:
                        all_evens = False
                cost += 1

        return cost
