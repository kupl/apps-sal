class Solution:
    def knightDialer(self, N: int) -> int:
        if N == 1:
            return 10

        navigation = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }

        memo = {}

        def get_num_distinct_dials(last_digit, N_left):
            if N_left == 0:
                return 1

            memo_key = (last_digit, N_left)
            if memo_key in memo:
                return memo[memo_key]

            result = sum([get_num_distinct_dials(next_digit, N_left - 1) for next_digit in navigation[last_digit]])
            memo[memo_key] = result
            return result

        return sum([get_num_distinct_dials(first_digit, N - 1) for first_digit in navigation.keys()]) % (10 ** 9 + 7)
