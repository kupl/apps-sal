class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        """
        monoqueue + prefixsum + sliding window
        """
        n = len(A)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
        end = 0
        res = float('inf')
        mono_queue = collections.deque()
        while end < n + 1:
            while mono_queue and prefix_sum[mono_queue[-1]] >= prefix_sum[end]:
                mono_queue.pop()
            while mono_queue and prefix_sum[end] - prefix_sum[mono_queue[0]] >= K:
                start_index = mono_queue.popleft()
                res = min(res, end - start_index)
            mono_queue.append(end)
            end += 1
        return res if res != float('inf') else -1
