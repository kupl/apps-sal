class Solution:
    def knightDialer(self, N: int) -> int:
        myMap = {1: [8, 6],
                 2: [7, 9],
                 3: [4, 8],
                 4: [0, 3, 9],
                 5: [],
                 6: [0, 1, 7],
                 7: [2, 6],
                 8: [1, 3],
                 9: [2, 4],
                 0: [4, 6],
                 -1: list(range(10))}
        cache = {}

        def dfs(start, level):
            if level == 0:
                return 1
            key = str(start) + str(level)
            if key in cache:
                return cache[key]
            else:
                ans = 0
                for number in myMap[start]:
                    ans += dfs(number, level - 1)
                cache[key] = ans
                return ans

        total = dfs(-1, N)
        return total % (10**9 + 7)
