class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:

        n, prefix, total, res = len(S), 0, S.count('1'), sys.maxsize
        for i in range(n + 1):
            res = min(res, prefix + len(S) - i - total + prefix)
            if i < n:
                prefix += 1 if S[i] == '1' else 0
        return res
