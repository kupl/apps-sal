class Solution:

    def knightDialer(self, n: int) -> int:
        len_start_number = {}
        mod_num = 1000000007
        len_start_number = {(1, i): 1 for i in range(0, 10)}
        for i in range(2, n + 1):
            len_start_number[i, 1] = (len_start_number[i - 1, 4] + len_start_number[i - 1, 8]) % mod_num
            len_start_number[i, 2] = len_start_number[i - 1, 7] * 2 % mod_num
            len_start_number[i, 4] = (len_start_number[i - 1, 1] + len_start_number[i - 1, 7] + len_start_number[i - 1, 0]) % mod_num
            len_start_number[i, 5] = 0
            len_start_number[i, 7] = (len_start_number[i - 1, 2] + len_start_number[i - 1, 4]) % mod_num
            len_start_number[i, 8] = len_start_number[i - 1, 1] * 2 % mod_num
            len_start_number[i, 0] = len_start_number[i - 1, 4] * 2 % mod_num
        count = 0
        for k in [0, 1, 2, 4, 5, 7, 8]:
            if k in [1, 4, 7]:
                count += 2 * len_start_number[n, k] % mod_num
            else:
                count += len_start_number[n, k] % mod_num
        return count % mod_num
