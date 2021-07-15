class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        M = max(arr)
        if M<0:
            return M
        
        kad = arr[:]
        curr = 0
        for i in range(len(arr)):
            kad[i] = max(0, curr+kad[i])
            curr = kad[i]
        
        curr = 0
        revkad = arr[:]
        for i in range(len(arr)-1,-1,-1):
            revkad[i] = max(0, curr+revkad[i])
            curr = revkad[i]
        
        ans = max(kad)
        for i in range(1,len(arr)-1):
            ans = max(ans, kad[i-1]+revkad[i+1])
        
        
        return ans
