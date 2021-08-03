class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        ans = 0
        mn = 0
        mp = 0
        for i in nums:
            if i == 0:
                mn, mp = 0, 0
            elif i > 0:
                mp += 1
                if mn != 0:
                    mn += 1
                else:
                    mn = 0
            else:
                omn = mn
                mn = mp + 1
                if omn != 0:
                    mp = omn + 1
                else:
                    mp = 0
            ans = max(mp, ans)
        return ans
