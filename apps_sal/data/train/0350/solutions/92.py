class Solution:

    def subarraysWithAtMostK(self, A: List[int], K: int) -> int:
        result = i = 0
        count = collections.Counter()
        for j in range(len(A)):
            if count[A[j]] == 0:
                K -= 1
            count[A[j]] += 1
            while K < 0:
                count[A[i]] -= 1
                if count[A[i]] == 0:
                    K += 1
                i += 1
            result += j - i + 1
        return result

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.subarraysWithAtMostK(A, K) - self.subarraysWithAtMostK(A, K - 1)
