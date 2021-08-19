class Solution:

    def knightDialer(self, n: int) -> int:
        next_move = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        mod_num = 10 ** 9 + 7
        dp_prev = [1] * 10
        for i in range(n - 1):
            dp_new = [0] * 10
            for num in range(10):
                phones_for_num = sum((dp_prev[x] for x in next_move[num])) % mod_num
                dp_new[num] = phones_for_num
            dp_prev = dp_new
        return sum(dp_prev) % mod_num
