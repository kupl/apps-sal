class Solution:
    def isInterleave(self, s1, s2, s3):
        if s1 == '' and s2 == '' and s3 == '':
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        paths = [[False for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        for i in range(1, len(s1) + 1):
            if s1[i - 1] == s3[i - 1]:
                paths[0][i] = True
            else:
                break
        for i in range(1, len(s2) + 1):
            if s2[i - 1] == s3[i - 1]:
                paths[i][0] = True
            else:
                break
        for i in range(1, len(s2) + 1):
            for j in range(1, len(s1) + 1):
                if ((paths[i][j - 1] is True and s1[j - 1] == s3[i + j - 1])

                            or (paths[i - 1][j] is True and s2[i - 1] == s3[i + j - 1])
                        ):
                    paths[i][j] = True
        return paths[len(s2)][len(s1)]
