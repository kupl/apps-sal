class Solution:
    def splitArraySameAverage(self, A: List[int]) -> bool:
        def dp(idx, rem, cnt):
            if cnt==0 and rem==0:
                return True
            
            if idx==N or cnt==0 or rem==0:
                return False
            
            if (idx, rem, cnt) in memo: return memo[(idx, rem, cnt)]
            
            res = False
            for i in range(idx, N):
                if A[i]>rem: break
                if dp(i+1, rem-A[i], cnt-1):
                    res = True
                    break
            
            memo[(idx, rem, cnt)] = res
            return res
        
        suma = sum(A)
        N = len(A)
        memo = {}
        A.sort()
        for i in range(1, N//2+1):
            if suma*i%N==0 and dp(0, suma*i/N, i):
                return True
            
        return False
