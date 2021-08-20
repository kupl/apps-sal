class Solution:

    def countVowelPermutation(self, n: int) -> int:
        if n < 1:
            return 0
        f = [[0] * 5, [0] * 5]
        f[1 & 1] = [1] * 5
        vowel = 'aeoui'
        for i in range(2, n + 1):
            f[i & 1][0] = (f[i - 1 & 1][3] + f[i - 1 & 1][1] + f[i - 1 & 1][4]) % (10 ** 9 + 7)
            f[i & 1][1] = (f[i - 1 & 1][0] + f[i - 1 & 1][4]) % (10 ** 9 + 7)
            f[i & 1][2] = f[i - 1 & 1][4] % (10 ** 9 + 7)
            f[i & 1][3] = (f[i - 1 & 1][2] + f[i - 1 & 1][4]) % (10 ** 9 + 7)
            f[i & 1][4] = (f[i - 1 & 1][1] + f[i - 1 & 1][2]) % (10 ** 9 + 7)
        return sum(f[n & 1]) % (10 ** 9 + 7)
