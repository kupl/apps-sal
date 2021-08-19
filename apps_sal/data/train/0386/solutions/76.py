class Solution:

    def countVowelPermutation(self, n: int) -> int:
        res = [[0 for i in range(5)] for j in range(n)]
        result = 0
        if n == 1:
            return 5
        for i in range(5):
            res[0][i] = 1
        for i in range(1, n):
            res[i][0] = res[i - 1][1] + res[i - 1][2] + res[i - 1][4]
            res[i][1] = res[i - 1][0] + res[i - 1][2]
            res[i][2] = res[i - 1][1] + res[i - 1][3]
            res[i][3] = res[i - 1][2]
            res[i][4] = res[i - 1][2] + res[i - 1][3]
        for i in range(5):
            result = (result + res[n - 1][i]) % 1000000007
        return result
