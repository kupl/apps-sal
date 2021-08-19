class Solution:

    def knightDialer(self, n: int) -> int:
        paths = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        counts = 0
        lookup = {}
        for i in range(10):
            counts += self.traverse(i, paths, lookup, n, 0)
        return counts % (10 ** 9 + 7)

    def traverse(self, starting, paths, lookup, n, level):
        if level == n - 1:
            return 1
        counts = 0
        for path in paths[starting]:
            if (path, level + 1) not in lookup:
                lookup[path, level + 1] = self.traverse(path, paths, lookup, n, level + 1)
            counts += lookup[path, level + 1]
        return counts % (10 ** 9 + 7)
