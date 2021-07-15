class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [[0]*5 for i in range(n)]
        for i in range(len(dp[0])):
            dp[0][i] = 1 
        dic = {'a':'e','e':'ai','i':'aeou','o':'iu','u':'a'}
        mapping = {'a':0,'e':1,'i':2,'o':3,'u':4}
        for i in range(1,n):
            for char in 'aeiou':
                inda = mapping[char]
                for val in dic[char]:
                    indb = mapping[val]
                    dp[i][indb] += dp[i-1][inda]
        return sum(dp[-1])%(10**9 + 7)
        
        
        
        

