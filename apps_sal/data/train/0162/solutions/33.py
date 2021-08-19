class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import lru_cache

        @lru_cache(maxsize=None)
        def memo_solve(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if text1[p1] == text2[p2]:
                return 1 + memo_solve(p1 + 1, p2 + 1)
            else:
                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))
        return memo_solve(0, 0)
        "\n        def memo_solve(p1, p2):\n            \n            # Base case: If either string is now empty, we can't match\n            # up anymore characters.\n            if p1 == len(text1) or p2 == len(text2):\n                return 0\n            \n            # Option 1: We don't include text1[p1] in the solution.\n            option_1 = memo_solve(p1 + 1, p2)\n            \n            # Option 2: We include text1[p1] in the solution, as long as\n            # a match for it in text2 at or after p2 exists.\n            first_occurence = text2.find(text1[p1], p2)\n            option_2 = 0\n            if first_occurence != -1:\n                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)\n            \n            # Return the best option.\n            return max(option_1, option_2)\n                \n        return memo_solve(0, 0)"
