class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        ret = 0
        n = len(A)
        mapping = {v:i for i, v in enumerate(A)}
        
        for i in range(n):
            for j in range(i+1, n):
                prev_, next_ = A[j], A[i]+A[j]
                length = 2
                while next_ in mapping:
                    length += 1
                    prev_, next_ = next_, prev_+next_
                
                if length > 2:
                    ret = max(ret, length)
        
        return ret
