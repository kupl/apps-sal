class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        return shortest_subarray(A, K)


def shortest_subarray(A: List[int], K: int) -> int:
    n = len(A)
    sums = [0] * (n + 1)
    for i in range(n):
        sums[i + 1] = sums[i] + A[i]
    result = n + 1
    q = deque()
    for i, total in enumerate(sums):
        while q and total < sums[q[-1]]:
            q.pop()
        while q and total - sums[q[0]] >= K:
            result = min(result, i - q.popleft())
        q.append(i)
    return result if result <= n else -1
