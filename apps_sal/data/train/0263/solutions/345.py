class Solution:

    def knightDialer(self, n: int) -> int:
        dic = {0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
        MOD = 10 ** 9 + 7
        cache = {}

        def dfs(start, digit):
            key = (start, digit)
            if key in cache:
                return cache[key]
            if digit == 0:
                return 1
            if digit < 0:
                return 0
            ans = 0
            if dic.get(start, -1) == -1:
                return 0
            for neigh in dic[start]:
                ans += dfs(neigh, digit - 1)
            cache[key] = ans
            return ans
        count = 0
        for i in range(10):
            count = (count + dfs(i, n - 1)) % MOD
        return count
