class Solution:

    def kConcatenationMaxSum(self, A: List[int], k: int) -> int:
        if all((a <= 0 for a in A)):
            return 0
        total = sum(A)
        N = len(A)
        (startingAt, endingAt) = [[-sys.maxsize] * N for _ in range(2)]
        bestStart = bestEnd = -sys.maxsize
        MOD = 10 ** 9 + 7
        for i in range(N):
            startingAt[N - 1 - i] = A[N - 1 - i] + (startingAt[N - i] if N - i < N and startingAt[N - i] > 0 else 0)
            endingAt[i] = A[i] + (endingAt[i - 1] if i - 1 >= 0 and endingAt[i - 1] > 0 else 0)
            (bestStart, bestEnd) = (max(bestStart, startingAt[N - 1 - i]), max(bestEnd, endingAt[i]))
        if k == 1:
            return bestStart
        return max(bestStart, max(0, endingAt[N - 1] + max(0, total * (k - 2)) + max(0, startingAt[0]))) % MOD
