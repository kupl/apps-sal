class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        self.mod = 10 ** 9 + 7
        self.memo = {}

        def helper(rolls, last, freq):
            if rolls == 0:
                return 1
            if (rolls, last, freq) in self.memo:
                return self.memo[rolls, last, freq]
            count = 0
            for j in range(len(rollMax)):
                if j == last:
                    if freq < rollMax[j]:
                        count += helper(rolls - 1, j, freq + 1) % self.mod
                else:
                    count += helper(rolls - 1, j, 1) % self.mod
            self.memo[rolls, last, freq] = count % self.mod
            return count % self.mod
        count = 0
        for i in range(6):
            count += helper(n - 1, i, 1)
        return count % self.mod
