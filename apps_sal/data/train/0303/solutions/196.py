class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        def dfs(start, memo):
            if start in memo:
                return memo[start]
            N = len(A)
            if start >= N:
                return 0
            maxSum = 0
            maxEle = 0
            for i in range(start, min(N, start + K)):
                maxEle = max(maxEle, A[i])
                maxSum = max(maxSum, maxEle * (i - start + 1) + dfs(i + 1, memo))
            memo[start] = maxSum
            return maxSum
        return dfs(0, {})

#         max_heap = []
#         counter = collections.defaultdict(int)
#         N = len(A)
#         result = []
#         for i in range(K):
#             heappush(max_heap, -A[i])
#             counter[A[i]] += 1

#         for i, n in enumerate(A):
#             if i+k < N:
#                 result.append(-heap[0][0])
