class Solution:
    def knightDialer(self, n: int) -> int:
        jump = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [6, 2],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6]
        }
        memo = {}

        def helper(cur, k):
            if (cur, k) in memo:
                return memo[(cur, k)]
            if k == 0:
                return 0
            elif k == 1:
                return 1
            res = 0
            for item in jump[cur]:
                res += helper(item, k - 1)
            memo[(cur, k)] = res % (10**9 + 7)
            return res

        res = 0
        for i in range(10):
            res += helper(i, n)
        return res % (10**9 + 7)
