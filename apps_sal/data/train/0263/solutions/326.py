class Solution:

    def __init__(self):
        self.paths = {1: [8, 6], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}

    def knightDialer(self, n: int) -> int:  # 3

        # ways(0, 3)
        # ways(4, 2)
        # ways(3, 1)
        # ways(4, 0)
        # return 0
        # ways(8, 0) # 0
        # ways(9, 1)
        # ways(0, 1)
        # ways(6, 2)

        cache = {}

        # @lru_cache
        def ways(number, turns):
            if turns < 2:
                return turns

            key = (number, turns)
            if key in cache:
                return cache[key]

            total_ways = 0
            for new_number in self.paths[number]:
                total_ways += ways(new_number, turns - 1)

            cache[key] = total_ways

            return cache[key]

        total_ways = 0  # 0
        for i in range(10):
            total_ways += ways(i, n)
        return total_ways % (10**9 + 7)
