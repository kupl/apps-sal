class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        
        class UniqueCounter(object):    
            def __init__(self):
                self.non_zero = 0
                self.counts = collections.defaultdict(int)
                
            def add(self, x):
                if self.counts[x] == 0:
                    self.non_zero += 1
                self.counts[x] += 1
                
            def remove(self, x):
                self.counts[x] -= 1
                if self.counts[x] == 0:
                    self.non_zero -= 1

            def count(self):
                return self.non_zero
                
        def subarrays_with_max_K(A, K):
            j = 0
            uc = UniqueCounter()
            uc.add(A[0])
            answer = 0
            for i in range(len(A)):
                while j < len(A) and uc.count() <= K:
                    j += 1
                    if j < len(A):
                        uc.add(A[j])
                answer += j - i
                uc.remove(A[i])
            return answer
            
        return subarrays_with_max_K(A, K) - subarrays_with_max_K(A, K - 1)

