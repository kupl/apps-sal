class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        N = len(s) - 1
        res = 1
        for m in range(1 << N):
            I = [i for i in range(N) if (m >> i) & 1] + [N]
            K = len(I)
            ss = {s[:I[0] + 1]}
            for k in range(K - 1):
                ss.add(s[I[k] + 1: I[k + 1] + 1])
            # print(ss)
            if len(ss) == K:
                res = max(res, K)
        return res
