class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        self.mcnt = 0
        par = {}
        sz = {}

        def find(i):
            while i != par[i]:
                par[i] = par[par[i]]
                i = par[i]
            return i

        def union(i, j):
            x = find(i)
            y = find(j)
            if x == y:
                return
            if sz[x] == m:
                self.mcnt -= 1
            if sz[y] == m:
                self.mcnt -= 1

            if sz[x] <= sz[y]:
                sz[y] += sz[x]
                par[x] = y

                if sz[y] == m:
                    self.mcnt += 1
            else:
                sz[x] += sz[y]
                par[y] = x

                if sz[x] == m:
                    self.mcnt += 1

        count = 1
        ans = -1
        target = set()
        for i in arr:
            if i not in par:
                par[i] = i
                sz[i] = 1
                if m == 1:
                    self.mcnt += 1

            if i - 1 in par:
                union(i - 1, i)

            if i + 1 in par:
                union(i, i + 1)

            if self.mcnt > 0:
                ans = count
            count += 1

        return ans
