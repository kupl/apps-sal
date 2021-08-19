class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        # if n == 1:
        #     return 1.0
        # else:
        #     return 0.5

        if n == 1:
            return 1.0
        sum_results = 0.0
        for i in range(2, n + 1):
            p = 1 / i * (1 + sum_results)
            sum_results += p
        return p
