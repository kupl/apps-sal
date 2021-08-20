class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        opt = [[0] * (target + 1) for _ in range(d + 1)]
        opt[0][0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                sum_children = 0
                face_val = 1
                while face_val <= f and j - face_val >= 0:
                    sum_children += opt[i - 1][j - face_val] % mod
                    face_val += 1
                opt[i][j] = sum_children % mod
        return opt[d][target]
