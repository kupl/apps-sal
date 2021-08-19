class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        P = [0]
        for x in A:
            P.append(P[-1] + x)
        q = collections.deque()
        min_length_K = -1
        for (j, Pj) in enumerate(P):
            while len(q) > 0 and P[q[-1]] >= Pj:
                q.pop()
            while len(q) > 0 and Pj - P[q[0]] >= K:
                if min_length_K == -1 or j - q[0] < min_length_K:
                    min_length_K = j - q[0]
                q.popleft()
            q.append(j)
        return min_length_K
