class Solution:

    def knight(self, n, current, memo):
        knight_mp = {1: {8, 6}, 2: {9, 7}, 3: {4, 8}, 4: {3, 9, 0}, 5: {}, 6: {7, 1, 0}, 7: {2, 6}, 8: {3, 1}, 9: {2, 4}, 0: {6, 4}}
        if n == 1:
            return 1
        if (current, n) in memo:
            return memo[current, n]
        res = 0
        for item in knight_mp.get(current, set()):
            res += self.knight(n - 1, item, memo)
        memo[current, n] = res
        return res

    def knightDialer(self, n: int) -> int:
        knight_mp = {1: {8, 6}, 2: {9, 7}, 3: {4, 8}, 4: {3, 9, 0}, 5: {}, 6: {7, 1, 0}, 7: {2, 6}, 8: {3, 1}, 9: {2, 4}, 0: {6, 4}}
        prev = [1 for _ in range(0, 10)]
        mod = 10 ** 9 + 7
        for step in range(1, n):
            curr = [0 for _ in range(0, 10)]
            for cell in range(0, 10):
                for neighbor in knight_mp.get(cell, set()):
                    curr[cell] += prev[neighbor]
            prev = curr
        return sum(prev) % mod
