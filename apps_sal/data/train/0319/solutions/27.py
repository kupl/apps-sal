class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.mem = dict()
        self.n = len(stoneValue)
        self.values = stoneValue
        (me, oppo) = self.dfs(0)
        if me > oppo:
            return 'Alice'
        elif oppo > me:
            return 'Bob'
        return 'Tie'

    def dfs(self, idx):
        if idx >= self.n:
            return (0, 0)
        if idx in self.mem:
            return self.mem[idx]
        oppo = 0
        rv = -float('inf')
        tmp = 0
        for i in range(idx, min(self.n, idx + 3)):
            (rv1, rv2) = self.dfs(i + 1)
            tmp += self.values[i]
            if rv < tmp + rv2:
                rv = tmp + rv2
                oppo = rv1
        self.mem[idx] = (rv, oppo)
        return self.mem[idx]
