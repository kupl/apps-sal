class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        max_floors = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
        for k in range(1, K + 1):
            for t in range(1, N + 1):
                max_floors[k][t] = 1 + max_floors[k - 1][t - 1] + max_floors[k][t - 1]
        for t in range(N):
            if max_floors[K][t] >= N:
                return t
        return N
