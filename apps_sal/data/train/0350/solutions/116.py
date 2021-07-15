from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysWithAtMostKDistinct(A, K) - self.subarraysWithAtMostKDistinct(A, K-1)
    
    def subarraysWithAtMostKDistinct(self, A, K):
        window = Counter()
        j = 0
        res = 0
        for i in range(len(A)):
            c = A[i]
            
            window[c] += 1
            
            while len(window) > K:
                last = A[j]
                window[last] -= 1
                if window[last] == 0:
                    del window[last]
                j += 1
            # print(j, i)
            res += i-j + 1
        return res
