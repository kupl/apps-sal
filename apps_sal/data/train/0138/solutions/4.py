class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        last = {1: -1}
        pro = 1
        ans = 0
        for (i, c) in enumerate(nums):
            pro = c * pro / abs(pro) if pro != 0 else 0
            if pro > 0:
                ans = max(i - last[1], ans)
            elif pro < 0:
                if -1 in last:
                    ans = max(ans, i - last[-1])
                else:
                    last[-1] = i
            elif pro == 0:
                pro = 1
                last = {}
                last[1] = i
        return ans
