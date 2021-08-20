class Solution:

    def getMaxLen(self, nums: List[int]) -> int:

        def helper(arr):
            inds = []
            for (i, num) in enumerate(arr):
                if num < 0:
                    inds.append(i)
            if len(inds) % 2 == 0:
                return len(arr)
            else:
                first = max(inds[0], len(arr) - inds[0] - 1)
                second = max(inds[-1], len(arr) - inds[-1] - 1)
                return max(first, second)
        temp = []
        for (i, num) in enumerate(nums):
            if num == 0:
                temp.append(i)
        pos = []
        if temp:
            if nums[:temp[0]]:
                pos.append(nums[:temp[0]])
            for i in range(0, len(temp) - 1):
                pos.append(nums[temp[i] + 1:temp[i + 1]])
            if nums[temp[-1] + 1:]:
                pos.append(nums[temp[-1] + 1:])
        else:
            pos.append(nums)
        ans = 0
        for arr in pos:
            ans = max(ans, helper(arr))
        return ans
