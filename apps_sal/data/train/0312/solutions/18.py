from typing import List


class Solution:
    def shortestSubarray(self, arr: List[int], K: int) -> int:
        pr_arr = [arr[i] for i in range(len(arr))]
        for i in range(1, len(arr)):
            pr_arr[i] = pr_arr[i - 1] + arr[i]

        q = []
        q.append((0, -1))
        min_window_size = float('inf')
        for i, val in enumerate(pr_arr):
            while len(q) > 0 and q[len(q) - 1][0] >= val:
                q.pop()

            q.append((val, i))

            window_sum = val - q[0][0]
            while window_sum >= K:
                min_window_size = min(min_window_size, i - q[0][1])
                q.pop(0)

                if len(q) == 0:
                    break

                window_sum = val - q[0][0]

        if min_window_size == float('inf'):
            return -1
        return min_window_size
