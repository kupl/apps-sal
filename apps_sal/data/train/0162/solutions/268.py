class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        pre = [0] * (len(text1) + 1)
        cur = [0] * (len(text2) + 1)

        for col in reversed(list(range(len(text1)))):
            for row in reversed(list(range(len(text2)))):
                if (text1[col] == text2[row]):
                    cur[row] = 1 + pre[row + 1]
                else:
                    cur[row] = max(pre[row], cur[row + 1])
            pre, cur = cur, pre
        return pre[0]
