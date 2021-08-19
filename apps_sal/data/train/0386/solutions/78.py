class Solution:

    def countVowelPermutation(self, n: int) -> int:
        dp_array = [[0] * 5 for _ in range(n + 1)]
        dp_array[1] = [1, 1, 1, 1, 1]
        for i in range(2, n + 1):
            dp_array[i][0] = dp_array[i - 1][1] + dp_array[i - 1][2] + dp_array[i - 1][4]
            dp_array[i][1] = dp_array[i - 1][0] + dp_array[i - 1][2]
            dp_array[i][2] = dp_array[i - 1][1] + dp_array[i - 1][3]
            dp_array[i][3] = dp_array[i - 1][2]
            dp_array[i][4] = dp_array[i - 1][2] + dp_array[i - 1][3]
        return sum(dp_array[n]) % (10 ** 9 + 7)
