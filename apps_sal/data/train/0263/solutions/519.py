class Solution:
    def knightDialer(self, N: int) -> int:

        if N == 1:
            return 10
        ends_in = [0 if i == 5 else 1 for i in range(10)]
        mod = 1e9 + 7

        for i in range(N - 1):
            next_ends_in = [0 for _ in range(10)]
            next_ends_in[0] = (ends_in[4] + ends_in[6]) % mod
            next_ends_in[1] = (ends_in[6] + ends_in[8]) % mod
            next_ends_in[2] = (ends_in[7] + ends_in[9]) % mod
            next_ends_in[3] = (ends_in[4] + ends_in[8]) % mod
            next_ends_in[4] = (ends_in[3] + ends_in[9] + ends_in[0]) % mod
            next_ends_in[6] = (ends_in[1] + ends_in[7] + ends_in[0]) % mod
            next_ends_in[7] = (ends_in[2] + ends_in[6]) % mod
            next_ends_in[8] = (ends_in[1] + ends_in[3]) % mod
            next_ends_in[9] = (ends_in[2] + ends_in[4]) % mod
            ends_in = next_ends_in

        return int(sum(ends_in) % mod)
