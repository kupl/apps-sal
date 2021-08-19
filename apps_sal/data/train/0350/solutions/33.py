from collections import Counter


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atMostK(A, K):
            counts = Counter()
            (left, result) = (0, 0)
            for right in range(len(A)):
                if counts[A[right]] == 0:
                    K -= 1
                counts[A[right]] += 1
                while K < 0:
                    counts[A[left]] -= 1
                    if counts[A[left]] == 0:
                        K += 1
                    left += 1
                result += right - left + 1
            return result
        return atMostK(A, K) - atMostK(A, K - 1)
