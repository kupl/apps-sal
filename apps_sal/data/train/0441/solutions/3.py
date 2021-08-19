class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        # number of ways to write N as a sum of consecutive posititive integers
        # with k consecutive integers, you can have
        # 1, 2, ..., k or 2, 3, ..., k + 1 or 3, 4, ..., k + 2
        # 1, 2, ..., k or 1, 2, ..., k, k or 1, 2, ..., k, k, k
        # => N can be written as a sum of k consecutive integers if (N - (1 + 2 + ... k)) mod k == 0
        # (1 + 2 + ... k) = k (k + 1) / 2
        num_ways = 1
        n = 2
        while (n * (n + 1) / 2) <= N:
            if (N - (n * (n + 1) / 2)) % n == 0:
                num_ways += 1
            n += 1
        return num_ways
