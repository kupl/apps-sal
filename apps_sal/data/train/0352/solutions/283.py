class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_predecessor(str1, str2):
            if len(str1) + 1 != len(str2):
                return False
            else:
                for i in range(len(str2)):
                    if str1 == str2[:i] + str2[i+1:]:
                        return True
                return False
        l = len(words)
        words.sort(key=len)
        mat = [[0 for j in range(l)] for i in range(l)]
        mat_max = 0
        for i in range(l):
            for j in range(i, l):
                str1, str2 = words[i], words[j]
                if is_predecessor(str1, str2):
                    mat[i][j] = mat[i][i] + 1
                    mat[j][j] = max(mat[j][j], mat[i][j])
                    mat_max = max(mat_max, mat[i][j])
        return mat_max + 1
