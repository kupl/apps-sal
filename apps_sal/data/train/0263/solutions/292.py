class Solution:

    def knightDialer(self, N: int) -> int:
        steps = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        def dfs(start, remain, seen):
            if remain == 0:
                return 1
            if (start, remain) in seen:
                return seen[start, remain]
            ans = 0
            for s in steps[start]:
                ans += dfs(s, remain - 1, seen)
            seen[start, remain] = ans
            return ans
        ans = 0
        seen = {}
        for i in range(10):
            ans += dfs(i, N - 1, seen)
        return ans % (10 ** 9 + 7)
