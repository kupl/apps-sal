class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        if len(arr) == 0:
            return 0

        mod = int(10**9) + 7
        v = arr[:]
        pre = [0]
        suf = [0]
        ans = msuf = mpre = 0

        for x in arr:
            if k > 1:
                v.append(x)
            ans += x
            pre.append(pre[-1] + x)
            mpre = max(mpre, pre[-1])

        for x in arr[::-1]:
            suf.append(suf[-1] + x)
            msuf = max(msuf, suf[-1])

        if ans > 0 and k >= 2:
            return (((k - 2) * ans) % mod + msuf + mpre) % mod

        maxi = 0
        for x in v:
            maxi = max(0, maxi + x)
            ans = max(ans, maxi)

        return ans % mod
