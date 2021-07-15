class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.at_most_K(A, K) - self.at_most_K(A, K - 1)
        
    
    def at_most_K(self, A, k):
        left = 0
        counter = collections.Counter()
        diff = 0
        result = 0
        for right in range(len(A)):
            counter[A[right]] += 1
            if counter[A[right]] == 1:
                diff += 1
            while diff > k:
                counter[A[left]] -= 1
                if counter[A[left]] == 0:
                    diff -= 1
                left += 1
            result += right - left + 1
        return result
