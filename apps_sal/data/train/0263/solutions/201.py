possible = {-1: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 0: [4, 6], 1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [0, 3, 9], 5: [], 6: [0, 1, 7], 7: [2, 6], 8: [1, 3], 9: [2, 4]}
cache = {}


class Solution:

    def knightDialer(self, n: int) -> int:
        total = self.helper(-1, n, 0) % 1000000007
        return total

    def helper(self, num, n, total):
        if (num, n) in cache:
            total += cache[num, n]
            return total
        nxt = possible[num]
        total_begin = total
        if n == 1:
            total += len(nxt)
        else:
            for num_next in nxt:
                total = self.helper(num_next, n - 1, total) % 1000000007
        cache[num, n] = total - total_begin
        return total
