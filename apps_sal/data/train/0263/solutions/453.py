class Solution:

    def knightDialer(self, n: int) -> int:
        N = n
        transition = {1: [6, 8], 2: [7, 9], 3: [4, 8], 4: [3, 9, 0], 5: [], 6: [1, 7, 0], 7: [2, 6], 8: [1, 3], 9: [2, 4], 0: [4, 6]}
        self.count = 0
        self.mem = {}

        def dfs(cur, steps):
            if steps == 2:
                return len(transition[cur])
            else:
                tmp = 0
                if (cur, steps) in self.mem:
                    return self.mem[cur, steps]
                for neigh in transition[cur]:
                    tmp += dfs(neigh, steps - 1)
                self.mem[cur, steps] = tmp
                return self.mem[cur, steps]
        if N == 1:
            return 10
        for i in range(10):
            self.count += dfs(i, N)
        return self.count % (10 ** 9 + 7)
