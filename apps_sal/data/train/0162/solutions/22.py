class Solution:

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) < len(text1):
            (text1, text2) = (text2, text1)
        previous = [0] * (len(text1) + 1)
        current = [0] * (len(text1) + 1)
        for col in reversed(range(len(text2))):
            for row in reversed(range(len(text1))):
                if text2[col] == text1[row]:
                    current[row] = 1 + previous[row + 1]
                else:
                    current[row] = max(previous[row], current[row + 1])
            (previous, current) = (current, previous)
        return previous[0]
        "\n        # Make a grid of 0's with len(text2) + 1 columns \n        # and len(text1) + 1 rows.\n        dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]\n        \n        # Iterate up each column, starting from the last one.\n        for col in reversed(range(len(text2))):\n            for row in reversed(range(len(text1))):\n                # If the corresponding characters for this cell are the same...\n                if text2[col] == text1[row]:\n                    dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]\n                # Otherwise they must be different...\n                else:\n                    dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])\n        \n        # The original problem's answer is in dp_grid[0][0]. Return it.\n        return dp_grid[0][0]\n        "
        "\n        from functools import lru_cache\n        @lru_cache(maxsize=None)\n        def memo_solve(p1, p2):\n            \n            # Base case: If either string is now empty, we can't match\n            # up anymore characters.\n            if p1 == len(text1) or p2 == len(text2):\n                return 0\n            \n            # Recursive case 1.\n            if text1[p1] == text2[p2]:\n                return 1 + memo_solve(p1 + 1, p2 + 1)\n            \n            # Recursive case 2.\n            else:\n                return max(memo_solve(p1, p2 + 1), memo_solve(p1 + 1, p2))\n            \n        return memo_solve(0, 0)\n        "
        "\n        def memo_solve(p1, p2):\n            \n            # Base case: If either string is now empty, we can't match\n            # up anymore characters.\n            if p1 == len(text1) or p2 == len(text2):\n                return 0\n            \n            # Option 1: We don't include text1[p1] in the solution.\n            option_1 = memo_solve(p1 + 1, p2)\n            \n            # Option 2: We include text1[p1] in the solution, as long as\n            # a match for it in text2 at or after p2 exists.\n            first_occurence = text2.find(text1[p1], p2)\n            option_2 = 0\n            if first_occurence != -1:\n                option_2 = 1 + memo_solve(p1 + 1, first_occurence + 1)\n            \n            # Return the best option.\n            return max(option_1, option_2)\n                \n        return memo_solve(0, 0)"
