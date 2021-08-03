class Solution:
    def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
        MOD = 1000000000 + 7
        K = len(evil)
        umap = [[[[0 for x in range(2)] for j in range(2)] for k in range(K)] for l in range(n)]
        lps = list()

        def computeLPS(s: str) -> List[int]:
            N = len(s)
            dp = [0 for i in range(N)]

            j = 0
            for i in range(1, N):
                while j > 0 and s[i] != s[j]:
                    j = dp[j - 1]
                if s[i] == s[j]:
                    j += 1
                dp[i] = j
            return dp

        def dfs(sp, ep, leftB, rightB) -> int:
            if ep >= K:
                return 0
            if sp >= n:
                return 1

            if umap[sp][ep][leftB][rightB] == 0:
                i = s1[sp] if leftB == 1 else 'a'
                j = s2[sp] if rightB == 1 else 'z'

                while ord(i) <= ord(j):
                    nxt = ep
                    while nxt > 0 and i != evil[nxt]:
                        nxt = lps[nxt - 1]

                    res = umap[sp][ep][leftB][rightB] + dfs(sp + 1, (nxt + 1 if evil[nxt] == i else 0), (1 if (leftB == 1 and i == s1[sp]) else 0), (1 if (rightB == 1 and i == s2[sp]) else 0))
                    umap[sp][ep][leftB][rightB] = res % MOD
                    i = chr(ord(i) + 1)
            return umap[sp][ep][leftB][rightB]

        lps = computeLPS(evil)
        return dfs(0, 0, 1, 1)
