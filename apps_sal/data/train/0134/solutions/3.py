class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        # https://leetcode.com/problems/numbers-with-repeated-digits/discuss/592922/Python-Well-commented-solution-with-easy-to-follow-recursion
        memo = {}

        def f(digits_of_N, i, digits_used, any_digit):
            if i == k:
                return 1

            key = (i, digits_used, any_digit)
            if key in memo:
                return memo[key]
            cnt = 0
            min_digit = 1 if i == 0 else 0
            max_digit = 9 if any_digit else digits_of_N[i]
            for d in range(min_digit, max_digit + 1):
                if digits_used & (1 << d) != 0:
                    continue
                cnt += f(digits_of_N, i + 1, digits_used | (1 << d), any_digit or (d < digits_of_N[i]))

            memo[key] = cnt
            return cnt
        if N <= 9:
            return 0
        k = len(str(N))
        cnt = 0
        for i in range(1, k):
            all_possible_ints = 9 * 10**(i - 1)
            ints_with_unique_digits = 9
            nb_choices = 9
            for j in range(1, i):
                ints_with_unique_digits *= nb_choices
                nb_choices -= 1
            cnt += all_possible_ints - ints_with_unique_digits

        all_ints_with_k_digits = N - int('9' * (k - 1))
        digits_of_N = [int(d) for d in str(N)]
        ints_with_unique_k_digits = f(digits_of_N, 0, 0, False)
        cnt += all_ints_with_k_digits - ints_with_unique_k_digits

        return cnt
