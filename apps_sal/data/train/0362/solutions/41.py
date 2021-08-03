class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        self.visited = 0
        hm = {}
        for n, i in enumerate(hats):
            for j in i:
                if j not in hm:
                    hm[j] = [n]
                else:
                    hm[j].append(n)
        keys = list(hm.keys())
        self.saved = {}

        def helper(index):
            if (index, self.visited) in self.saved:
                return self.saved[(index, self.visited)]

            if self.visited == ((1 << len(hats)) - 1):
                return 1
            if index == len(keys):
                return 0
            count = 0

            for i in hm[keys[index]]:
                if not self.visited & (1 << i):
                    self.visited |= 1 << i
                    count += helper(index + 1)
                    self.visited ^= 1 << i
            self.saved[(index, self.visited)] = count + helper(index + 1)
            return self.saved[(index, self.visited)]
        return helper(0) % (10 ** 9 + 7)
