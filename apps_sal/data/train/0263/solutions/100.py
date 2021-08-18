class Solution:
    def knightDialer(self, n: int) -> int:
        M = 10**9 + 7
        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0],
                 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        prior_n = [1] * 10

        for hops in range(2, n + 1):
            curr_n = [0] * 10
            for num, count in enumerate(prior_n):
                for nbr in moves[num]:
                    curr_n[nbr] += count
                    curr_n[nbr] %= M

            prior_n = curr_n
        return sum(prior_n) % M
