class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        table = {}

        def helper(t1, t2, i, j, table):
            if table.get((i, j)) != None:
                return table[(i, j)]

            n = len(t1)
            m = len(t2)

            if m <= j or n <= i:
                return 0

            v = t1[i]
            idx = t2.find(v, j)
            if idx != -1:
                r = max(helper(t1, t2, i + 1, j, table), helper(t1, t2, i + 1, idx + 1, table) + 1)
                table[(i, j)] = r
            else:
                r = helper(t1, t2, i + 1, j, table)
                table[(i, j)] = r
            return table[(i, j)]

        return helper(text1, text2, 0, 0, table)
