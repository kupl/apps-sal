class Solution:

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        cache = [[0 for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                if str1[i - 1] == str2[j - 1]:
                    cache[i][j] = 1 + cache[i - 1][j - 1]
                else:
                    cache[i][j] = max(cache[i][j - 1], cache[i - 1][j])
        print(cache)
        (i, j) = (len(str1), len(str2))
        ans = ''
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans = str1[i - 1] + ans
                i -= 1
                j -= 1
            elif cache[i][j - 1] > cache[i - 1][j]:
                ans = str2[j - 1] + ans
                j -= 1
            else:
                ans = str1[i - 1] + ans
                i -= 1
        print(str1, str2, ans, i, j)
        if i > 0:
            ans = str1[:i] + ans
            i -= 1
        if j > 0:
            ans = str2[:j] + ans
            j -= 1
        return ans
