class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        to_mod = 10 ** 9 + 7
        # the index end at, num of consecutive
        seq_num = [[0 for j in range(rollMax[i] + 1)] for i in range(6)]
        for i in range(6):
            if rollMax[i] > 0:
                seq_num[i][1] = 1
        for l in range(2, n + 1):
            new_seq_num = [[0 for i in range(rollMax[j] + 1)] for j in range(6)]
            seq_sum = [sum(seq_num[i]) % to_mod for i in range(6)]
            for i in range(6):
                for j in range(6):
                    if i != j:
                        new_seq_num[i][1] += seq_sum[j]
                    else:
                        for k in range(2, min(n, rollMax[i]) + 1):
                            new_seq_num[i][k] = seq_num[i][k - 1]
            seq_num = new_seq_num
        result = 0
        for i in range(6):
            result += sum(seq_num[i])
            result = result % to_mod
        return result
