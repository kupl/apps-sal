class Solution:
    NEIGHBORS = ((4, 6), (6, 8), (7, 9), (4, 8), (0, 3, 9), (), (0, 1, 7), (2, 6), (1, 3), (2, 4))
    cache = {}

    def get_neighbors(self, n: int) -> Tuple[int]:
        return self.NEIGHBORS[n]

    def knightDialer(self, n: int) -> int:
        results = 0
        prior = [1] * 10
        for _ in range(n - 1):
            current = [0] * 10
            for pos in range(10):
                for neighbor in self.get_neighbors(pos):
                    current[pos] += prior[neighbor] % 1000000007
            prior = current
        return sum(prior) % 1000000007
