class Solution:

    def knightDialer(self, n: int) -> int:
        achievable = {}
        achievable[0] = [4, 6]
        achievable[1] = [6, 8]
        achievable[2] = [7, 9]
        achievable[3] = [4, 8]
        achievable[4] = [0, 3, 9]
        achievable[5] = []
        achievable[6] = [0, 1, 7]
        achievable[7] = [2, 6]
        achievable[8] = [1, 3]
        achievable[9] = [2, 4]
        f1 = [1 for _ in range(10)]
        m = 10 ** 9 + 7
        for i in range(1, n):
            f2 = [0 for _ in range(10)]
            for j in range(10):
                f2[j] = sum((f1[l] for l in achievable[j])) % m
            f1 = f2.copy()
        return sum(f1) % m
