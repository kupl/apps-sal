import bisect
class Solution:
    ans = [0 for i in range(100001)]
    def getMaxLen(self, nums: List[int]) -> int:
        def solve(arr):
            s1, s2 = set(), set()
            s1.add(-1)
            ret = 0
            cnt = 0
            n = len(arr)
            for i, c in enumerate(arr):
                cnt += 0 if c > 0 else 1
                if cnt % 2 == 0:
                    s1.add(i)
                else:
                    s2.add(i)
            if s1:
                ret = max(s1) - min(s1)
            if s2:
                ret = max(max(s2) - min(s2), ret)
            # print(s1, s2, ret)
            return ret
        ans = 0
        l = 0
        for i, c in enumerate(nums):
            if c == 0:
                ans = max(ans, solve(nums[l:i]))
                l = i + 1
        ans = max(ans, solve(nums[l:]))
        return ans
