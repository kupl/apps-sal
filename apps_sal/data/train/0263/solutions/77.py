class Solution:
    def knightDialer(self, n: int) -> int:
        reachFrom = {1: [8, 6], 2: [7, 9], 3: [4, 8], 4: [0, 9, 3], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        prevdp = [1 for _ in range(10)]
        curdp = [0 for _ in range(10)]
        for iteration in range(1, n):
            curdp = [0 for _ in range(10)]
            for i in range(10):
                for nbor in reachFrom[i]:
                    curdp[i] += prevdp[nbor]
            prevdp = curdp.copy()
        ans = 0
        for i in range(10):
            ans += prevdp[i]
        return ans % (10**9 + 7)
