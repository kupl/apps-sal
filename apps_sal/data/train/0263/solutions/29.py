class Solution:

    def __init__(self):
        self.paths = {1: [8, 6], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

    def knightDialer(self, n: int) -> int:
        constant = 10 ** 9 + 7
        if n == 0:
            return 0
        prev_cache = [1 for i in range(10)]
        cache = [0 for i in range(10)]
        for i in range(n - 1):
            for j in range(10):
                total_sum = 0
                for adj_num in self.paths[j]:
                    total_sum += prev_cache[adj_num]
                cache[j] = total_sum
            (prev_cache, cache) = (cache, prev_cache)
        return sum(prev_cache) % constant
