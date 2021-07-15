from functools import lru_cache


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        
        @lru_cache(None)
        def tallest_support_given_diff_of_pair(n, diff):
            # max(L if (L, L - diff) can be built by rods[:n])
            if n == 0:
                return 0 if diff == 0 else float('-inf')

            L = rods[n - 1]
            no_new_rod = tallest_support_given_diff_of_pair(n - 1, diff)
            new_rod_on_taller = tallest_support_given_diff_of_pair(
                n - 1,
                abs(diff - L),
            ) + min(diff, L)
            new_rod_on_shorter = tallest_support_given_diff_of_pair(n - 1, diff + L)
            return max(no_new_rod, new_rod_on_taller, new_rod_on_shorter)

        return tallest_support_given_diff_of_pair(len(rods), diff=0)

