class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.atMost(A, K) - self.atMost(A, K - 1)

    def atMost(self, A, k):
        left = res = 0
        freq = collections.Counter()
        for right in range(len(A)):
            if freq[A[right]] == 0:
                k -= 1
            freq[A[right]] += 1
            while k < 0:
                freq[A[left]] -= 1
                if freq[A[left]] == 0:
                    k += 1
                left += 1
            res += right - left + 1
        return res
