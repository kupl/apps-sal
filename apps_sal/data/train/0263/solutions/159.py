class Solution:
    def knightDialer(self, n: int) -> int:
        arr = [[0 for i in range(10)] for i in range(n)]
        mappings = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
        }
        mod = 10**9 + 7
        arr[0] = [1 for i in range(10)]
        for i in range(1, n):
            for j in range(10):
                for k in mappings[j]:
                    arr[i][j] += arr[i - 1][k]
        return sum(arr[n - 1]) % mod
