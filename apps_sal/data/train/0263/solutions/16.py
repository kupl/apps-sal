class Solution:

    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dic = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [4, 2]}
        counts = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        for k in range(n - 1):
            new = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for i in range(10):
                for j in dic[i]:
                    new[j] = (new[j] + counts[i]) % mod
            counts = new
        return sum(counts) % mod
