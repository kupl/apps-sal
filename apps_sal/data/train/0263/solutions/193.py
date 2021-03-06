class Solution:

    def __init__(self):
        self.mem = dict()

    def knightDialer(self, n: int) -> int:
        reach = [[4, 6], [6, 8], [7, 9], [4, 8], [0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        counts = [1] * 10
        for i in range(n - 1):
            counts2 = [sum((counts[k] for k in reach[j])) for j in range(10)]
            counts = counts2
        return sum(counts) % (10 ** 9 + 7)
