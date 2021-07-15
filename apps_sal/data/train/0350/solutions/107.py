from collections import Counter

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def at_most(K):
            window = Counter()
            left = right = 0
            res = 0
            while right < len(A):
                window[A[right]] += 1
                while len(window) > K:
                    window[A[left]] -= 1
                    if not window[A[left]]:
                        del window[A[left]]
                    left += 1
                
                res += right - left + 1
                right += 1
            
            return res
        
        return at_most(K) - at_most(K - 1)

