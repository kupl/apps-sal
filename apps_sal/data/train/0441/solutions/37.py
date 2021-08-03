class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        counter = 0

        for num_terms in range(1, N + 1):
            difference = num_terms * (num_terms - 1) // 2
            remainder = N - difference
            if remainder <= 0:
                break
            if remainder % num_terms == 0:
                counter += 1

        return counter
