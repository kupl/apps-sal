class Solution:
    MOD = 10 ** 9 + 7

    def longestPrefix(self, s: str) -> str:
        N = len(s)
        left_i, right_i = 0, N - 1
        left_val = right_val = 0

        best_left = -1
        right_multiplier = 1
        for i in range(N - 1):
            left_char, right_char = s[i], s[N - i - 1]
            left_val = left_val * 26 + (ord(left_char) - ord('a'))
            right_val = (ord(right_char) - ord('a')) * right_multiplier + right_val
            right_multiplier *= 26

            left_val %= Solution.MOD
            right_val %= Solution.MOD
            right_multiplier %= Solution.MOD
            if left_val == right_val:
                best_left = i

        return s[:best_left + 1]
