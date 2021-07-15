class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        def helper( memo, p1, p2 ):

            if p1 >= len(text1) or p2 >= len(text2):
                return 0
            
            if (p1, p2) in memo:
                return memo[(p1, p2)]
            
            if text1[p1] == text2[p2]:
                return 1 + helper( memo, p1+1, p2+1 )

            c1 = helper( memo, p1+1, p2 )
            c2 = helper( memo, p1, p2+1 )

            memo[(p1, p2)] = max( c1, c2 )
            return memo[(p1, p2)]

        # need to memoize the p1, p2, and length
        memo = {}
        return helper( memo, 0, 0 )
