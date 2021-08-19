import collections


class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        cum_sum = 0
        queue = collections.deque([(-1, 0)])
        result = len(A) + 1
        for i, v in enumerate(A):
            cum_sum += v
            # find any matches and remove them, since will never have a better match
            while queue and cum_sum - queue[0][1] >= K:
                e = queue.popleft()
                #print('remove candidate from start:', e)
                result = min(result, i - e[0])
            # pop off any greater cum sums, which will never be a better target
            while queue and cum_sum <= queue[-1][1]:
                e = queue.pop()
                #print('remove greater from end:', e)

            queue.append((i, cum_sum))
            # print(queue)
        return result if result <= len(A) else -1
