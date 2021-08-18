class Solution:
    def mean(self, l):
        return sum(l) / len(l)

    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        DP = [self.mean(A[i:n]) for i in range(n)]

        for k in range(K - 1):
            for i in range(n):
                for j in range(i + 1, n):
                    DP[i] = max(DP[i], self.mean(A[i:j]) + DP[j])

        return DP[0]
