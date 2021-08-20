class Solution:

    def sumSubarrayMins(self, A: List[int]) -> int:
        (res, curr_sum, min_arr) = (0, 0, [(float('-inf'), -1)])
        for (i, a) in enumerate(A):
            while min_arr and a < min_arr[-1][0]:
                (b, j) = min_arr.pop()
                curr_sum -= b * (j - min_arr[-1][1])
            curr_sum += a * (i - min_arr[-1][1])
            min_arr.append((a, i))
            res += curr_sum
        return res % (10 ** 9 + 7)
