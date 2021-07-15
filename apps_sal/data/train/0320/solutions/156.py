class Solution:
    # naive is BFS, but too costly.
    # Start from nums by greedily trace back, whenever there is an odd number, take one action to make it even by reduce 1. If everything is even, half them by taking one action.
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        while True:
            for i in range(len(nums)):  # take 1 action each to make elem from odd to even
                if nums[i] % 2:
                    nums[i] -= 1
                    count += 1
            all_zero = True
            for i in range(len(nums)):  # take one action to half all elem
                if nums[i] != 0:
                    all_zero = False
                nums[i] //= 2
            if all_zero:
                return count
            count += 1
        return count

