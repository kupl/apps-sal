class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        if not A:
            return -1
        if len(A) == 1:
            if A[0] < K:
                return -1
            return 1
        min_length = float('inf')
        temp = [0]
        for i in A:
            temp.append(i + temp[-1])
        queue = []
        for (c, v) in enumerate(temp):
            while queue and v <= temp[queue[-1]]:
                queue.pop()
            while queue and v - temp[queue[0]] >= K:
                min_length = min(min_length, c - queue.pop(0))
            queue.append(c)
        if min_length == float('inf'):
            return -1
        return min_length
