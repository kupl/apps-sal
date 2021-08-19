class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        prefix_sums = [0]
        prefix_sum = 0
        for a in A:
            prefix_sum += a
            prefix_sums.append(prefix_sum)
        from collections import deque
        mono_q = deque()
        min_len = len(A) + 1
        for (y, Py) in enumerate(prefix_sums):
            while mono_q and Py <= prefix_sums[mono_q[-1]]:
                mono_q.pop()
            while mono_q and Py - prefix_sums[mono_q[0]] >= K:
                min_len = min(y - mono_q.popleft(), min_len)
            mono_q.append(y)
        return min_len if min_len < len(A) + 1 else -1
