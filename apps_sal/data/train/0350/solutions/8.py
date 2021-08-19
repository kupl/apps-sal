class Solution:
    from collections import Counter

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:

        def atMostK(K):
            i = 0
            count = 0
            counts = Counter()
            for j in range(len(A)):
                if counts[A[j]] == 0:
                    K -= 1
                counts[A[j]] += 1
                while K < 0:
                    counts[A[i]] -= 1
                    if counts[A[i]] == 0:
                        K += 1
                    i += 1
                count += j - i + 1
            return count
        return atMostK(K) - atMostK(K - 1)
