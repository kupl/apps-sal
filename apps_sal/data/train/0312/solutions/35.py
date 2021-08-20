class Solution:

    def shortestSubarray(self, A: List[int], K: int) -> int:
        S = [0]
        res = float('inf')
        for num in A:
            S.append(S[-1] + num)
        q = []
        for (i, s) in enumerate(S):
            while q and S[q[-1]] >= s:
                q.pop()
            while q and S[q[0]] + K <= s:
                cur_i = q.pop(0)
                res = min(res, i - cur_i)
            q.append(i)
        if res == float('inf'):
            return -1
        else:
            return res
