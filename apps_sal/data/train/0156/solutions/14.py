class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)

        t = str1 + str2
        cur = ['' for _ in range(n + 1)]
        prev = ['' for _ in range(n + 1)]

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0:
                    cur[j] = str2[:j]
                elif j == 0:
                    cur[j] = str1[:i]
                else:
                    a, b = str1[i - 1], str2[j - 1]

                    if a == b:
                        cur[j] = prev[j - 1] + a
                    else:
                        if len(prev[j]) < len(cur[j - 1]):
                            cur[j] = prev[j] + a
                        else:
                            cur[j] = cur[j - 1] + b
            prev = cur
            cur = ['' for _ in range(n + 1)]

        return prev[-1]
