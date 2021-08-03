class Solution:
    def knightDialer(self, N: int) -> int:

        hop_map = {1: [6, 8],
                   2: [7, 9],
                   3: [4, 8],
                   4: [0, 3, 9],
                   6: [0, 1, 7],
                   7: [2, 6],
                   8: [1, 3],
                   9: [2, 4],
                   0: [4, 6]}

        memo = {(i, 1): 1 for i in range(10)}

        def num_hops(key: int, N: int):

            if N == 1:
                return 1

            if key in [1, 4, 7]:
                key += 2
            elif key == 5:
                return 0

            if (key, N) in memo:
                return memo[(key, N)]

            sum_ = 0
            for v in hop_map[key]:
                sum_ += num_hops(v, N - 1)

            memo[(key, N)] = sum_ % (10**9 + 7)
            return sum_

        sum_ = 0
        for i in range(10):
            sum_ += num_hops(i, N) % (10**9 + 7)
        return sum_ % (10**9 + 7)
