class Solution:
     def numOfSubarrays(self,A) -> int:
        n = len(A)
        MOD = pow(10,9)+7
        dp_even,dp_odd = [0],[0]
        if A[0]%2:
            dp_odd[0] += 1
        else:
            dp_even[0] += 1

        ans = dp_odd[-1]
        
        for i in range(1,n):
            if A[i]%2:
                dp_odd.append( (dp_even[i-1]+1)%MOD )
                dp_even.append( dp_odd[i-1] )
            else:
                dp_odd.append( dp_odd[i-1] )
                dp_even.append( (dp_even[i-1]+1)%MOD )
            ans += dp_odd[i]
            ans %= MOD
        
        #print(dp_even,dp_odd)
        
        return ans
