class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        if len(s) <= k:
            return 0
        
        def num_change(w):#number need to change to become palindrome
            l,r=0,len(w)-1
            count=0
            while l<r:
                if w[l]!=w[r]:
                    count+=1
                l+=1
                r-=1
            return count
        
        def dp(i,k):
            if (i,k) not in memo:
                if k==1:
                    memo[i,k]=num_change(s[:i+1])
                else:
                    memo[i,k]=min(dp(j,k-1)+num_change(s[j+1:i+1]) for j in range(k-2,i))
            return memo[i,k]
        
        memo={}    
        n=len(s)
        return dp(n-1,k)
