class Solution:
    def longestArithSeqLength(self, A):
        dp = {}
        #dictionary of pairs (i pointer, dist)
        
        # i pointer iterates from 1index to the end
        for i in range(1, len(A)):
            # j pointer iterates from 0 to just left of i pointer then resets
            for j in range(0, len(A[:i])):
                
                #finds the difference of the two values
                d = A[i] - A[j]
                
                #checks to see if the same diff exists at j
                if (j, d) in dp:
                    #if j,d is in dp then add 1 because the value at i has the same difference and set that as i,d
                    dp[i, d] = dp[j, d] + 1
                #if not then its set to two because that accounts for the i,j as two integers
                else:
                    dp[i, d] = 2
                    
        #return what ever is the highest value of all the keys in the dictionary is
        return max(dp.values())
