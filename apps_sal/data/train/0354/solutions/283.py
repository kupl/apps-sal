MAX = 10 ** 9 + 7


class Solution:
    
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        D = [[0] * 6 for i in range(n + 1)]
        D[1] = [1] * 6
        seq_nums = [0] * (n + 1)
        seq_nums[0], seq_nums[1] = 1, 6
        for i in range(2, n + 1):
            for j in range(6):
                for k in range(1, min(rollMax[j], i) + 1):
                    D[i][j] = (D[i][j] + seq_nums[i - k] + MAX - D[i - k][j]) % MAX
                    
                seq_nums[i] = (seq_nums[i] + D[i][j]) % MAX
                
        return seq_nums[-1]
