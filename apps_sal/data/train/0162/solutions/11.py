class Solution:
    # approach 3
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        def print_grid(grid):
            for row in grid:
                print(row)

        dp_row = [0] * (len(s2) + 1)
        dp_row_pre = [0] * (len(s2) + 1)
        N, M = len(s1), len(s2)
        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if s1[i] == s2[j]:
                    dp_row[j] = dp_row_pre[j + 1] + 1
                else:
                    dp_row[j] = max(dp_row_pre[j], dp_row[j + 1])
            dp_row_pre, dp_row = dp_row, dp_row_pre
            # print(\"update row=\", i, \", col=\", j)
            # print_grid(dp_grid)
        return dp_row_pre[0]

    # approach 1: recursive memorization
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         @lru_cache(maxsize=None)
#         def memo_solve(p1, p2):
#             if p1 == len(text1) or p2 == len(text2):
#                 return 0

#             # option 1: we don't include text1[p1] in the solution
#             option_1 = memo_solve(p1 + 1, p2)

#             # option 2: we include p1 in the solution, as long as there is a match in p2
#             first_occurrence = text2.find(text1[p1], p2)
#             option_2 = 0
#             if first_occurrence != -1:
#                 option_2 = 1 + memo_solve(p1 + 1, first_occurrence + 1)

#             return max(option_1, option_2)

#         return memo_solve(0, 0)

      # approach 2
#     def longestCommonSubsequence(self, s1: str, s2: str) -> int:

#         @lru_cache(maxsize=None)
#         def mem_solve(p1: int, p2: int) -> int:
#             # base case
#             if p1 == len(s1) or p2 == len(s2):
#                 return 0

#             # option 1 match the first letter
#             if s1[p1] == s2[p2]:
#                 return 1 + mem_solve(p1 + 1, p2 + 1)

#             # option 2
#             return max(mem_solve(p1, p2 + 1), mem_solve(p1 + 1, p2))

#         return mem_solve(0, 0)
