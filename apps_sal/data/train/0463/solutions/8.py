class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return 0
        if(n == 2):
            return abs(nums[1] - nums[0])

        base = 0
        for i in range(n - 1):
            base = base + abs(nums[i + 1] - nums[i])
        res = base
        for i in range(1, n - 1):
            if(res < base + abs(nums[i + 1] - nums[0]) - abs(nums[i + 1] - nums[i])):
                res = base + abs(nums[i + 1] - nums[0]) - abs(nums[i + 1] - nums[i])

        for i in range(1, n - 1):
            if(res < base + abs(nums[i - 1] - nums[n - 1]) - abs(nums[i] - nums[i - 1])):
                res = base + abs(nums[i - 1] - nums[n - 1]) - abs(nums[i] - nums[i - 1])

        currMax = (nums[0], nums[1])
        currMin = (nums[0], nums[1])
        for i in range(1, n - 1):
            curr = (nums[i], nums[i + 1])
            if(min(currMax) > max(curr)):
                if(res < base + 2 * (min(currMax) - max(curr))):
                    res = base + 2 * (min(currMax) - max(curr))

            if(max(currMin) < min(curr)):
                if(res < base + 2 * (min(curr) - max(currMin))):
                    res = base + 2 * (min(curr) - max(currMin))
            if(min(curr) > min(currMax)):
                currMax = curr
            if(max(curr) < max(currMin)):
                currMin = curr

        return res
