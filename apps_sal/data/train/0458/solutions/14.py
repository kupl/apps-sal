class Solution:

    def minSubarray(self, A: List[int], p: int) -> int:
        n = len(A)
        dp = [0] * (n + 1)
        for (i, a) in enumerate(A):
            dp[i + 1] = (dp[i] + a) % p
        if not dp[-1]:
            return 0
        ret = n
        dic = dict()
        for (i, d) in enumerate(dp):
            dic[d] = i
            t = (d + p - dp[-1]) % p
            if t in dic:
                ret = min(ret, i - dic[t])
        return ret if ret < n else -1
