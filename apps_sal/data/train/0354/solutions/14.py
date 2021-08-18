class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        faces = len(rollMax)
        record = [[0] * (faces + 1) for _ in range(n + 1)]
        record[0][faces] = 1
        for i in range(faces):
            record[1][i] = 1
        record[1][faces] = 6
        for i in range(2, n + 1):
            for j in range(faces):
                for k in range(1, rollMax[j] + 1):
                    if i - k < 0:
                        break
                    record[i][j] += record[i - k][faces] - record[i - k][j]
            record[i][faces] = sum(record[i])
        return record[-1][faces] % (10**9 + 7)
