class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        def dp(idx, L, target):
            if L==0 and target==0:
                return True
            
            if idx==N or L==0 or target<0:
                return False
            
            if (idx, L, target) in memo: return memo[(idx, L, target)]
            memo[(idx, L, target)] = A[idx]<=target and dp(idx+1, L-1, target-A[idx]) or dp(idx+1, L, target)
            return memo[(idx, L, target)]       

        total = sum(A)
        N = len(A)
        
        for i in range(1, len(A)//2+1):
            sub_sum = total*i/N
            memo = {}
            if sub_sum == int(sub_sum) and dp(0, i, int(sub_sum)):
                return True
            
        return False

