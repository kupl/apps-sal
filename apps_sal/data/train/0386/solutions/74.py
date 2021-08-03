class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5

        T = {
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }

        dp = {l: [0 for i in range(n)] for l in 'aeiou'}
        for letter in 'aeiou':
            dp[letter][1] = len(T[letter])

        for i in range(2, n):
            for l in 'aeiou':
                total = 0
                for r in T[l]:
                    total += dp[r][i - 1] % 1000000007
                dp[l][i] = total

        return sum(dp[letter][n - 1] for letter in 'aeiou') % 1000000007
