class Solution:

    def numTeams(self, rating: List[int]) -> int:

        def ascend(nums, curLargest, count):
            if count == 3:
                return 1
            if not nums:
                return 0
            total = 0
            for i in range(len(nums)):
                if nums[i] > curLargest:
                    total += ascend(nums[i + 1:], nums[i], count + 1)
            return total

        def descend(nums, curSmallest, count):
            if count == 3:
                return 1
            if not nums:
                return 0
            total = 0
            for i in range(len(nums)):
                if nums[i] < curSmallest:
                    total += descend(nums[i + 1:], nums[i], count + 1)
            return total
        return ascend(rating, 0, 0) + descend(rating, float('inf'), 0)
