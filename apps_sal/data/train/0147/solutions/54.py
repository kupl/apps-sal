import heapq


class Solution:

    def maxPerformance(self, n: int, S: List[int], E: List[int], k: int) -> int:
        tmp = []
        for (x, y) in zip(S, E):
            tmp.append([y, x])
        tmp.sort(reverse=True)
        stack = []
        sums = 0
        res = 0
        for i in range(n):
            nk = tmp[i][0]
            sums += tmp[i][1] - (heapq.heappop(stack) if len(stack) == k else 0)
            heapq.heappush(stack, tmp[i][1])
            res = max(res, nk * sums)
        return res % 1000000007
