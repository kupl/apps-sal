class Solution:
    def minOperations(self, nums: List[int]) -> int:
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
            if all_evens:
                for i in range(len(nums)):
                    nums[i] = nums[i] // 2
                cost += 1

        return cost
