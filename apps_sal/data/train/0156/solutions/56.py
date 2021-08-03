class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        i, j = m, n
        lcs = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                lcs.append(str1[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    i -= 1
                else:
                    j -= 1

        lcs.reverse()
        insert_1 = defaultdict(list)
        idx = 0

        for i in range(m):
            if idx < len(lcs) and str1[i] == lcs[idx]:
                idx += 1
            else:
                insert_1[idx].append(str1[i])

        insert_2 = defaultdict(list)
        idx = 0

        for i in range(n):
            if idx < len(lcs) and str2[i] == lcs[idx]:
                idx += 1
            else:
                insert_2[idx].append(str2[i])

        ans = ''

        for i in range(idx):
            ans += ''.join(insert_1[i]) + ''.join(insert_2[i]) + lcs[i]

        ans += ''.join(insert_1[idx]) + ''.join(insert_2[idx])
        return ans
