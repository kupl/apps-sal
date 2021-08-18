class Solution:
    def distinctEchoSubstrings(self, s):
        n = len(s)
        shash = [0] * (n + 1)
        spow = [1] * (n + 1)
        base = 29
        MOD = 10 ** 9 + 7
        seen = set()

        def gethash(i: int, j: int) -> int:
            return (shash[j] - shash[i - 1] * spow[j - i + 1] % MOD + MOD) % MOD

        for i in range(1, n + 1):
            shash[i] = (shash[i - 1] * base + ord(s[i - 1])) % MOD
            spow[i] = (spow[i - 1] * base) % MOD

        for i in range(n):
            for j in range(i + 1, n, 2):
                mid = (i + j) // 2
                lhash = gethash(i + 1, mid + 1)
                rhash = gethash(mid + 2, j + 1)
                if lhash == rhash:
                    seen.add(lhash)

        return len(seen)
