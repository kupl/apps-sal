class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1}
        follows = {'a': 'e', 'e': 'ai', 'i': 'aeou', 'o': 'iu', 'u': 'a'}
        mod = 10**9 + 7
        for _ in range(1, n):
            dp2 = {}
            for c, v in dp.items():
                for f in follows[c]:
                    dp2[f] = (dp2.get(f, 0) + v) % mod

            dp = dp2
        return sum(dp.values()) % mod
