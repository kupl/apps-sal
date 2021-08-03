class Solution:
    NEIGHBORS = (
        (4, 6),
        (6, 8),
        (7, 9),
        (4, 8),
        (0, 3, 9),
        (),
        (0, 1, 7),
        (2, 6),
        (1, 3),
        (2, 4)
    )

    def knightDialer(self, n: int) -> int:
        results = 0
        self.cache = {}
        for pos in range(10):
            results += self.traverse(pos, n)
            results %= 1000000007
        return results

    def traverse(self, pos: int, length: int) -> int:
        if length == 1:
            return 1
        if (pos, length) in self.cache:
            return self.cache[(pos, length)]
        jumps = 0
        for neighbor in self.get_neighbors(pos):
            jumps += self.traverse(neighbor, length - 1)

        jumps %= 1000000007
        self.cache[(pos, length)] = jumps
        return jumps

    def get_neighbors(self, n: int) -> Tuple[int]:
        return self.NEIGHBORS[n]
