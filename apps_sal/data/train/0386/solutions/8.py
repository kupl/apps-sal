class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0]*5 for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1
        vowels = ['a','e','i','o','u']
        for i in range(1,n):
            for idx,vowel in enumerate(vowels):
                if vowel == 'a':
                    dp[i][idx] += dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
                if vowel == 'e':
                    dp[i][idx] += dp[i-1][0] + dp[i-1][2]
                if vowel == 'i':
                    dp[i][idx] += dp[i-1][1] + dp[i-1][3]
                if vowel == 'o':
                    dp[i][idx] += dp[i-1][2]
                if vowel == 'u':
                    dp[i][idx] += dp[i-1][2] + dp[i-1][3]
                    
        return sum(dp[n-1]) % (10**9 + 7)
