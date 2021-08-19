from collections import Counter


class Solution:

    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        return self.helper(A, K) - self.helper(A, K - 1)

    def helper(self, A, K):
        currSum = 0
        d = Counter()
        i = 0
        for j in range(len(A)):
            d[A[j]] += 1
            while len(d) > K:
                d[A[i]] -= 1
                if not d[A[i]]:
                    del d[A[i]]
                i += 1
            currSum += j - i + 1
        return currSum
