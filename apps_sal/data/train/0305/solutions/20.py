class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        N = len(text)
        BASE = 27
        MOD = 1000000007
        s = set()
        hoffset = 1
        tord = [ord(x) - ord('a') + 1 for x in text]

        for offset in range(1, N // 2 + 1):
            hoffset = (hoffset * BASE) % MOD
            K = 0
            h = 0
            for j in range(N - offset):
                if text[j] == text[j + offset]:
                    K += 1
                    h = (h * BASE + tord[j + offset]) % MOD
                else:
                    K = 0
                    h = 0

                if K > offset:
                    h = (((h - hoffset * tord[j + offset]) % MOD) + MOD) % MOD
                    K -= 1

                if K == offset:
                    s.add(h)
        return len(s)
