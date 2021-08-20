class Solution:

    def numberOfArrays(self, s: str, k: int) -> int:
        cache = {}
        n = len(s)
        mod = 10 ** 9 + 7

        def process(i):
            if i == n:
                return 1
            elif s[i] == '0':
                return 0
            else:
                if not i in cache:
                    ans = 0
                    x = 0
                    j = 0
                    while i + j < n:
                        x = x * 10 + (ord(s[i + j]) - 48)
                        if x <= k:
                            ans += process(i + j + 1)
                            j += 1
                        else:
                            break
                    cache[i] = ans % mod
                return cache[i]
        return process(0)
