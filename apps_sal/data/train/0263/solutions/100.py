class Solution:
    def knightDialer(self, n: int) -> int:
        M = 10**9 + 7
        moves = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0],
                 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        # f(start, n) = number of ways to build an n-digit number starting
        # at number start
        # prior_n[i] = number of ways to build a 1-digit no. starting at i
        prior_n = [1] * 10

        # repeat process to generate array that gives number of
        # ways to build 2, 3, ... , n digit numbers starting at i
        for hops in range(2, n + 1):
            curr_n = [0] * 10
            # build on prior n results
            for num, count in enumerate(prior_n):
                # looking at numbers generated when we move nbr --> num --> ...
                for nbr in moves[num]:
                    curr_n[nbr] += count
                    curr_n[nbr] %= M

            # curr n becomes prior n
            prior_n = curr_n
        # return the sum of all n digit phone nums that can be created
        # by starting at num 0, 1, ... , 9
        return sum(prior_n) % M
