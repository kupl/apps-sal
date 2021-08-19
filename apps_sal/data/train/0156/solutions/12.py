class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        t = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    t[i][j] = t[i - 1][j - 1] + 1
                else:
                    t[i][j] = max(t[i - 1][j], t[i][j - 1])
        s = ''
        (i, j) = (n, m)
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                s = s + str1[i - 1]
                i -= 1
                j -= 1
            elif t[i - 1][j] > t[i][j - 1]:
                s = s + str1[i - 1]
                i -= 1
            else:
                s = s + str2[j - 1]
                j -= 1
        while i > 0:
            s += str1[i - 1]
            i -= 1
        while j > 0:
            s += str2[j - 1]
            j -= 1
        s = s[::-1]
        return s
