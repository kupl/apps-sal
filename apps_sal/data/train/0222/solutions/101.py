class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        
        res = 2
        S = set(A)  
        for i in range (len(A)-2):
            if A[i] * (res - 1) * (res - 2) > A[-1]:
                break
        
            for j in range (i+1, len(A)-1):
                cnt = 2
                a, b=A[j], A[i]+A[j]
                while b in S:
                    cnt+=1
                    a, b = b, a+b
                res = max(cnt, res)
        if res > 2:
            return res
        else:
            return 0
