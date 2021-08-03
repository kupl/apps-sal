class Solution:
    dp = [dict.fromkeys('aeiou', 1)]

    def countVowelPermutation(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        follows = {'a': 'e', 'e': 'ai', 'i': 'aeou', 'o': 'iu', 'u': 'a'}
        for i in range(len(self.dp), n):
            dp1 = dict.fromkeys('aeiou', 0)
            for j in 'aeiou':
                dp1[j] = sum(self.dp[-1][k] for k in follows[j]) % MOD
            self.dp.append(dp1)
        return sum(self.dp[n - 1].values()) % MOD
