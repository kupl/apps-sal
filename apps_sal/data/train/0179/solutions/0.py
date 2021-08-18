class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)

        def compLen(c):
            return 1 + len(str(c)) if c > 1 else 1

        @lru_cache(None)
        def dp(i, k):
            if (n - i) <= k:
                return {}
            x, res = s[i], {}
            if k:
                res = dp(i + 1, k - 1)
            keep = dp(i + 1, k)
            t = [(1 + min((leng for leng, _ in list(keep.values())), default=0), -1)]
            if x in keep:
                leng, negc = keep[x]
                leng, negc = (leng - compLen(-negc) + compLen(-negc + 1),
                              negc - 1)
                t.append((leng, negc))
            if x in res:
                t.append(res[x])
            res[x] = min(t)
            return res

        m = dp(0, k)
        return min((leng for leng, _ in list(m.values())), default=0)
