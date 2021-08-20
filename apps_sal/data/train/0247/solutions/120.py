from collections import deque
from itertools import accumulate


class Solution:

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        (x, n) = (list(accumulate(arr, initial=0)), len(arr))
        (s, d) = ([], {})
        for i in range(n + 1):
            y = x[i] - target
            if y in d:
                s.append([i - d[y], d[y], i])
            d[x[i]] = i
        for k in range(len(s) - 2, -1, -1):
            s[k][0] = min(s[k][0], s[k + 1][0])
        (ans, queue) = (float('inf'), deque([]))
        for (d, i, j) in s:
            while queue and queue[0][-1] <= i:
                ans = min(ans, queue.popleft()[0] + d)
            queue.append((j - i, i, j))
        return ans if ans < float('inf') else -1
