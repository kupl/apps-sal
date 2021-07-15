class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        A.sort()
        dp = {i:1 for i in A}
        res = 0
        for idd, number in enumerate(A):
            
            for inner, inumber in enumerate(A[:idd]):
                if number % inumber == 0 and ((number // inumber) in dp):
                    dp[number] += dp[inumber] * dp[number // inumber]
            
            res += dp[number]
            res = res % (10 ** 9 + 7)
        
        return res

