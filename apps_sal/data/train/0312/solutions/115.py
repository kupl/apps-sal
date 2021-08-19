class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        p = [0]
        p[0] = A[0]
        for i in range(1, len(A)):
            p.append(p[i - 1] + A[i])
        s = []
        s.append((-1, 0))
        min_len = float('inf')
        for i in range(len(p)):
            while s and p[i] - s[0][1] >= K:
                min_len = min(min_len, i - s[0][0])
                s.pop(0)
            while s and p[i] <= s[-1][1]:
                s.pop()
            s.append((i, p[i]))
        if min_len != float('inf'):
            return min_len
        else:
            return -1
