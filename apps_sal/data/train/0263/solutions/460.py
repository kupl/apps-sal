class Solution:

    def knightDialer(self, n: int) -> int:
        mod = 10 ** 9 + 7
        phone = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 0]]
        moves = ((2, 1), (1, 2), (2, -1), (1, -2), (-2, 1), (-1, 2), (-2, -1), (-1, -2))

        @lru_cache(None)
        def helper(row, col, left):
            if not 0 <= row <= 3 or not 0 <= col <= 2 or phone[row][col] == 0:
                return 0
            if left <= 0:
                return 1
            ans = 0
            for (r, c) in moves:
                if 0 <= row + r <= 3 and 0 <= col + c <= 2 and (phone[row + r][col + c] == 1):
                    ans += helper(row + r, col + c, left - 1)
            return ans
        ans = 0
        for row in range(4):
            for col in range(3):
                if phone[row][col] == 1:
                    ans += helper(row, col, n - 1)
        return ans % mod
