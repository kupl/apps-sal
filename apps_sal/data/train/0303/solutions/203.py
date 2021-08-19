class Solution:

    def maxSumAfterPartitioning(self, A: List[int], k: int) -> int:
        L = len(A)
        vis = {}

        def pos(n):
            if n >= L:
                return 0
            if n in vis:
                return vis[n]
            currmax = A[n]
            ans = A[n] + pos(n + 1)
            for i in range(1, k):
                n1 = n + i
                if n1 >= L:
                    break
                currmax = max(currmax, A[n1])
                ans = max(ans, currmax * (i + 1) + pos(n1 + 1))
            vis[n] = ans
            return vis[n]
        return pos(0)
