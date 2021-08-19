class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (mxh, mnh) = ([], [])
        i = j = 0
        ans = 0
        while i < len(nums):
            if j < len(nums) and (not mxh or not mnh or abs(mxh[0][0] + mnh[0][0]) <= limit):
                heappush(mnh, [nums[j], j])
                heappush(mxh, [-nums[j], j])
                j += 1
            else:
                if not mxh or not mnh or abs(mxh[0][0] + mnh[0][0]) <= limit:
                    ans = max(ans, j - i)
                else:
                    ans = max(ans, j - i - 1)
                i += 1
                while mxh and mxh[0][1] < i:
                    heappop(mxh)
                while mnh and mnh[0][1] < i:
                    heappop(mnh)
        return ans
