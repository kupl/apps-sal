from collections import Counter
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        W1 = Counter()
        W2 = Counter()
        l1 = 0
        l2 = 0
        res = 0
        
        for i in range(len(A)):
            W1[A[i]] += 1
            W2[A[i]] += 1
            
            while len(W1) > K:
                W1[A[l1]] -= 1
                if W1[A[l1]] == 0:
                    del W1[A[l1]]
                l1 += 1
            
            while len(W2) > K-1:
                W2[A[l2]] -= 1
                if W2[A[l2]] == 0:
                    del W2[A[l2]]
                l2 += 1
            
            res += l2 - l1
        return res
