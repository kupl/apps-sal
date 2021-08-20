class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        d = [[10000] * (len2 + 1) for _ in range(len1 + 1)]
        d[0][0] = 0
        for i in range(len1 + 1):
            for j in range(len2 + 1):
                if i < len1:
                    d[i + 1][j] = min(d[i + 1][j], d[i][j] + 1)
                if j < len2:
                    d[i][j + 1] = min(d[i][j + 1], d[i][j] + 1)
                if i < len1 and j < len2 and (str1[i] == str2[j]):
                    d[i + 1][j + 1] = min(d[i + 1][j + 1], d[i][j] + 1)
        pos1 = len1
        pos2 = len2
        ans = []
        while pos1 or pos2:
            while pos1 and pos2 and (str1[pos1 - 1] == str2[pos2 - 1]):
                ans.append(str1[pos1 - 1])
                pos1 -= 1
                pos2 -= 1
            while pos1 and d[pos1 - 1][pos2] + 1 == d[pos1][pos2]:
                ans.append(str1[pos1 - 1])
                pos1 -= 1
            while pos2 and d[pos1][pos2 - 1] + 1 == d[pos1][pos2]:
                ans.append(str2[pos2 - 1])
                pos2 -= 1
        ans.reverse()
        return ''.join(ans)
