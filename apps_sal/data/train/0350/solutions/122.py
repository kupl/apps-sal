from collections import defaultdict
class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def subArray(k):
            right = 0
            left = 0
            freq = collections.defaultdict(int)
            count = 0
            while right < len(A):
                freq[A[right]] += 1
                right += 1
                
                while len(freq) > k:
                    freq[A[left]] -= 1
                    if freq[A[left]] == 0:
                        del freq[A[left]]
                    left += 1
                count += right - left
            return count
        output = 0   
        output += subArray(K) - subArray(K-1)
        return output

