class Solution:
    def countVowelPermutation(self, n: int) -> int:
        
        vtoi = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
        itov = {0:'a', 1:'e', 2:'i', 3:'o', 4:'u'}
        
        prev = {'a': ['e', 'i', 'u'],
                'e': ['a', 'i'],
                'i': ['e', 'o'],
                'o': ['i'],
                'u': ['i', 'o']}
        dp = [[0 for _ in range(5)] for _ in range(n+1)]
        
        for j in range(5):
            dp[1][j] = 1
        
        for i in range(2, n+1):
            for j in range(5):
                for p in prev[itov[j]]:
                    dp[i][j] += dp[i-1][vtoi[p]]
    
        return sum(dp[-1]) % (10**9+7)
                
                

