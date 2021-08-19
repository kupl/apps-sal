class Solution:

    def knightDialer(self, n: int) -> int:
        if n == 0 or not n:
            return 0
        graph = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4]}

        @lru_cache(maxsize=None)
        def helper(left, curr):
            if left == 1:
                return 1
            cnt = 0
            for nei in graph[curr]:
                cnt += helper(left - 1, nei)
            return cnt
        ans = 0
        for i in range(10):
            ans += helper(n, i)
        return ans % (10 ** 9 + 7)
