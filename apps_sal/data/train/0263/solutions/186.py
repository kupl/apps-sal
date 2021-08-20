class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        MOD = 1000000007
        graph = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        prev = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        for _ in range(n - 1):
            val = [0] * 10
            for i in range(10):
                for x in graph[i]:
                    val[x] += prev[i]
            prev = val
        return sum(prev) % MOD
