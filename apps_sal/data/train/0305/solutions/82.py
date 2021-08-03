class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)

        MOD = 10**9 + 7
        BASE = 256

        ppow = defaultdict(int)
        ippow = defaultdict(int)
        ha = defaultdict(int)
        vis = defaultdict(bool)

        ippow[0] = ppow[0] = 1
        for i in range(n):
            ha[i] = (ha[i - 1] + ord(text[i]) * ppow[i]) % MOD
            ppow[i + 1] = ppow[i] * BASE % MOD
            ippow[i + 1] = pow(ppow[i + 1], -1, MOD)

        def compute(i, j):
            return (ha[j] - ha[i - 1]) * ippow[i] % MOD

        ret = 0
        for i in range(n):
            for j in range(i, n):
                if j + j - i + 1 < n:
                    c1 = compute(i, j)
                    if vis[c1]:
                        continue
                    u = j + 1
                    v = j + j - i + 1
                    if c1 == compute(u, v) and text[i:j + 1] == text[u:v + 1]:
                        vis[c1] = True
                        ret += 1

        return ret
