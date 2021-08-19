class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        table = [[[0, -1] for j in range(len(str2))] for i in range(len(str1))]
        if str1[0] == str2[0]:
            table[0][0][0] = 1
        else:
            table[0][0][0] = 2
            table[0][0][1] = 0
        for j in range(1, len(str2)):
            if str1[0] == str2[j]:
                table[0][j][0] = j + 1
                table[0][j][1] = j - 1
            else:
                (val1, val2) = (j + 1, table[0][j - 1][0])
                if val1 < val2:
                    table[0][j][0] = val1 + 1
                    table[0][j][1] = j
                else:
                    table[0][j][0] = val2 + 1
                    table[0][j][1] = j - 1
        for i in range(1, len(str1)):
            if str1[i] == str2[0]:
                table[i][0][0] = i + 1
            else:
                (val1, val2) = (table[i - 1][0][0], i + 1)
                if val1 < val2:
                    table[i][0][0] = val1 + 1
                    table[i][0][1] = 0
                else:
                    table[i][0][0] = i + 2
            for j in range(1, len(str2)):
                if str1[i] == str2[j]:
                    table[i][j][0] = table[i - 1][j - 1][0] + 1
                    table[i][j][1] = j - 1
                else:
                    (val1, val2) = (table[i - 1][j][0], table[i][j - 1][0])
                    if val1 < val2:
                        table[i][j][0] = val1 + 1
                        table[i][j][1] = j
                    else:
                        table[i][j][0] = val2 + 1
                        table[i][j][1] = j - 1
        result = ''
        (pos1, pos2) = (len(str1) - 1, len(str2) - 1)
        while True:
            if str1[pos1] == str2[pos2]:
                result = str1[pos1] + result
                (pos1, pos2) = (pos1 - 1, table[pos1][pos2][1])
            elif table[pos1][pos2][1] == pos2:
                result = str1[pos1] + result
                pos1 -= 1
            else:
                result = str2[pos2] + result
                pos2 = table[pos1][pos2][1]
            if pos1 < 0 or pos2 < 0:
                result = str1[0:pos1 + 1] + str2[0:pos2 + 1] + result
                break
        return result
