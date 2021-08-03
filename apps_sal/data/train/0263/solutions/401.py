class Solution:
    def knightDialer(self, n: int) -> int:
        cache = [[0 for i in range(n + 1)] for i in range(10)]
        for i in range(10):
            cache[i][1] = 1
        return self.hopper(n, cache) % (10 ** 9 + 7)

    def hopper(self, hops_left, cache):

        if hops_left == 1:
            return sum([cache[i][1] for i in range(10)])
        elif hops_left < 1:
            return 0
        else:
            for i in range(2, hops_left + 1):
                for j in range(10):
                    for nbr in self.nbrs(j):
                        cache[j][i] += cache[nbr][i - 1]

        return sum([cache[i][hops_left] for i in range(10)])

    def nbrs(self, ind):
        nbrs = {0: [4, 6],
                1: [6, 8],
                2: [9, 7],
                3: [4, 8],
                4: [3, 9, 0],
                5: [],
                6: [1, 7, 0],
                7: [6, 2],
                8: [1, 3],
                9: [4, 2]}

        return nbrs[ind]
