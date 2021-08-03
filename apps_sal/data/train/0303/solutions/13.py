from collections import deque


class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        dp = deque([0 for i in range(K)])
        for i in range(1, len(A) + 1):
            maxA, maxP = float('-inf'), float('-inf')
            for j in range(1, min(K, i) + 1):
                maxA = max(maxA, A[i - j])
                maxP = max(maxP, dp[-j] + j * maxA)
            dp.popleft()
            dp.append(maxP)
        return dp[-1]
