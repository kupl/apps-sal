import collections


class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        cum_sum = 0
        queue = collections.deque([(-1, 0)])
        result = len(A) + 1
        for (i, v) in enumerate(A):
            cum_sum += v
            if v > 0:
                while queue and cum_sum - queue[0][1] >= K:
                    e = queue.popleft()
                    result = min(result, i - e[0])
            else:
                while queue and cum_sum <= queue[-1][1]:
                    e = queue.pop()
            queue.append((i, cum_sum))
        return result if result <= len(A) else -1
