class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        # MOD = 10**9+7
        MOD = 2000000011
        textlen = len(text)
        half = textlen // 2
        f = [[0] * textlen for i in range(textlen)]
        HASH = {}
        for l in range(1, half + 1):
            HASH[l] = set()
            for i in range(textlen - l + 1):
                if l == 1:
                    f[i][i + l - 1] = ord(text[i]) - 97
                else:
                    f[i][i + l - 1] = (f[i][i + l - 2] * 26 + ord(text[i + l - 1]) - 97) % MOD
                HASH[l].add(f[i][i + l - 1])
        a = half + 1 if half % 2 == 1 else half + 2
        for l in range(a, half * 2 + 1, 2):
            HASH[l] = set()
            for i in range(textlen - l + 1):
                f[i][i + l - 1] = (f[i][i + l - 3] * 676 + (ord(text[i + l - 2]) - 97) * 26 + ord(text[i + l - 1]) - 97) % MOD
                HASH[l].add(f[i][i + l - 1])
        count = 0
        # print(HASH)
        # print(f)
        tmp = 1
        for l in range(1, half + 1):
            tmp = tmp * 26 % MOD
            for v in HASH[l]:
                if v * (tmp + 1) % MOD in HASH[2 * l]:
                    count += 1
        return count
