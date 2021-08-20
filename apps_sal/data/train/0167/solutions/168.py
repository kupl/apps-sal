class Solution:

    def superEggDrop(self, K: int, N: int) -> int:
        max_floors = [0 for _ in range(N + 1)]
        for k in range(1, K + 1):
            next_max_floors = [0 for _ in range(N + 1)]
            for t in range(1, N + 1):
                next_max_floors[t] = 1 + max_floors[t - 1] + next_max_floors[t - 1]
            max_floors = next_max_floors
        for t in range(N):
            if max_floors[t] >= N:
                return t
        return N
