class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        d = [[10000] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        d[0][0] = 0
        for i in range(len(str1) + 1):
            for j in range(len(str2) + 1):
                if d[i][j] == 10000:
                    continue
                if i < len(str1):
                    d[i + 1][j] = min(d[i + 1][j], d[i][j] + 1)
                if j < len(str2):
                    d[i][j + 1] = min(d[i][j + 1], d[i][j] + 1)
                if i < len(str1) and j < len(str2) and str1[i] == str2[j]:
                    d[i + 1][j + 1] = min(d[i + 1][j + 1], d[i][j] + 1)
        pos1 = len(str1)
        pos2 = len(str2)
        ans = []
        while pos1 or pos2:
            if pos1 and d[pos1 - 1][pos2] + 1 == d[pos1][pos2]:
                ans.append(str1[pos1 - 1])
                pos1 -= 1
                continue
            if pos2 and d[pos1][pos2 - 1] + 1 == d[pos1][pos2]:
                ans.append(str2[pos2 - 1])
                pos2 -= 1
                continue
            if pos1 and pos2 and str1[pos1 - 1] == str2[pos2 - 1]:
                ans.append(str1[pos1 - 1])
                pos1 -= 1
                pos2 -= 1
                continue
        ans.reverse()
        return ''.join(ans)
