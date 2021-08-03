class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        n = len(text)
        result = 0
        seen = set()
        BASE = 27
        MOD = 10 ** 9
        hashs = [0] * (n + 1)
        pows = [1] * (n + 1)
        for i in range(n):
            hashs[i + 1] = (hashs[i] * BASE + ord(text[i]) - 96) % MOD
            pows[i + 1] = (pows[i] * BASE) % MOD

        def h(i, j): return (hashs[j + 1] - (hashs[i] * pows[j - i + 1]) % MOD) % MOD

        for i in range(n):
            l = i
            r = i + 1
            while r < n:
                h1 = h(i, l)
                h2 = h(l + 1, r)
                if h1 == h2 and h1 not in seen:
                    result += 1
                    seen.add(h1)
                l += 1
                r += 2
        return result
