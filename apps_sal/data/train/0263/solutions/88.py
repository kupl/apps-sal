class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        graph = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        MOD = 1000000007
        prev = [1, 1, 1, 1, 1, 0, 1, 1, 1, 1]
        for _ in range(n - 1):
            val = [0] * 10
            for i in range(10):
                for x in graph[i]:
                    val[x] += prev[i]
            prev = val
        return sum(prev) % MOD
