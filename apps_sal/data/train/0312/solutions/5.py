class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        dq = deque([[0, 0]])
        curr_sum = 0
        min_size = len(A) + 1
        for i in range(len(A)):
            curr_sum += A[i]
            while dq and curr_sum - dq[0][1] >= K:
                min_size = min(min_size, i - dq.popleft()[0] + 1)
            while dq and curr_sum <= dq[-1][1]:
                dq.pop()
            dq.append([i + 1, curr_sum])
        return min_size if min_size != len(A) + 1 else -1
