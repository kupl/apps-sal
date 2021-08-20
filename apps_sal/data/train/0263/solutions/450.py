class Solution:
    mod = 10 ** 9 + 7
    phone = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 0]]
    moves = ((2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2))

    def knightDialer(self, n: int) -> int:

        @lru_cache(None)
        def helper(row, col, left):
            if left <= 0:
                return 1
            ans = 0
            for (r, c) in Solution.moves:
                if 0 <= row + r <= 3 and 0 <= col + c <= 2 and (Solution.phone[row + r][col + c] == 1):
                    ans += helper(row + r, col + c, left - 1)
            return ans
        ans = 0
        for row in range(4):
            for col in range(3):
                if Solution.phone[row][col] == 1:
                    ans += helper(row, col, n - 1)
        return ans % Solution.mod
