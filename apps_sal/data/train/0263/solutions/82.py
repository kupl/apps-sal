class Solution:

    def knightDialer(self, n: int) -> int:
        pos_map = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        num_vals = [1 if i != 5 else 0 for i in range(10)]
        mod_val = 10 ** 9 + 7
        if n == 1:
            return 10
        else:
            for num in range(1, n):
                temp = [0 for i in range(10)]
                for (i, count) in enumerate(num_vals):
                    for val in pos_map[i]:
                        temp[val] += count
                num_vals = temp
        return sum(num_vals) % mod_val
