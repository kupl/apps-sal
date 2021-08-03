class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        R = int(math.pow(10, 9) + 7)
        memo = {}

        options = {
            1: [6, 8],
            2: [7, 9],
            3: [8, 4],
            4: [3, 9, 0],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2],
            0: [4, 6]
        }

        def dfs(step, dig):
            if (step, dig) in memo:
                return memo[(step, dig)]

            if step == 1:
                return 1

            res = 0
            for d in options[dig]:
                res = (res + dfs(step - 1, d)) % R
            memo[(step, dig)] = res
            return res

        res = 0
        for d in range(0, 10, 1):
            if d == 5:
                continue
            res = (res + dfs(n, d)) % R

        return res
