class Solution:

    def getMaxLen(self, nums: List[int]) -> int:
        cn = 0
        cp = 0
        f = 0
        n = len(nums)
        pz = -1
        ans = 0
        for i in range(n):
            if nums[i] < 0:
                if f == 0:
                    fn = ln = i
                else:
                    ln = i
                cn += 1
                f = 1
            elif nums[i] > 0:
                cp += 1
            else:
                if cn % 2 == 0:
                    ans = max(ans, cn + cp)
                else:
                    z = cn + cp - min(i - ln, fn - pz)
                    ans = max(ans, z)
                f = 0
                cn = 0
                cp = 0
                pz = i
        if cn % 2 == 0:
            ans = max(ans, cn + cp)
        else:
            z = cn + cp - min(n - ln, fn - pz)
            ans = max(ans, z)
        return ans
