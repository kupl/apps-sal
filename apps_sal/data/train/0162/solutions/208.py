class Solution:
    def longestCommonSubsequence(self, str1: str, str2: str) -> int:
    
        cache = [ [-1]*len(str2) for _ in str1]

        
        def checkPosition(i1, i2):
            
            if i1 == len(str1) or i2 == len(str2):
                return 0
            
            #hashing
            if cache[i1][i2] != -1:
                return cache[i1][i2]

            # the characters match, so we can keep both
            if str1[i1] == str2[i2]:
                keep = 1 + checkPosition(i1+1, i2+1)

            else: 
                keep = -1

            skip1 = checkPosition(i1+1, i2)
            skip2 = checkPosition(i1, i2+1)
            
            best = max([keep, skip1, skip2])
            cache[i1][i2] = best
            return best

        return checkPosition(0,0)
    
    


