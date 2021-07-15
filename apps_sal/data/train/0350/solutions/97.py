from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        window1 = Counter()
        window2 = Counter()
        l1 = 0
        l2 = 0
        total = 0
        
        for r, c in enumerate(A):
            window1[c] += 1
            window2[c] += 1
            
            while(len(window1)>K):
                window1[A[l1]] -= 1
                if window1[A[l1]] == 0: del window1[A[l1]]
                l1 += 1
            while(len(window2)>K-1):
                window2[A[l2]] -= 1
                if window2[A[l2]] == 0: del window2[A[l2]]
                l2 += 1
                
            total += l2 - l1
        return total
       
            

