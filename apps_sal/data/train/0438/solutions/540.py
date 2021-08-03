class DSU:
    def __init__(self):
        self.N = 10**5 + 1
        self.parent = [i for i in range(self.N)]
        self.rank = [0 for _ in range(self.N)]
        self.comp = [1 for _ in range(self.N)]

    def find(self, i):
        if self.parent[i] == i:
            return i
        else:
            return self.find(self.parent[i])

    def union(self, i, j):
        x, y = self.find(i), self.find(j)

        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
            self.comp[x] += self.comp[y]
            self.comp[y] = 0

        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
            self.comp[y] += self.comp[x]
            self.comp[x] = 0

        else:
            self.parent[y] = x
            self.comp[x] += self.comp[y]
            self.comp[y] = 0
            self.rank[x] += 1


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = 10**5 + 1
        nums = [False for _ in range(N + 2)]
        d = DSU()

        cnt = [0 for _ in range(N + 2)]
        ret = -1

        for index, a in enumerate(arr):
            cnt[d.comp[d.find(a)]] += 1

            if nums[a - 1]:
                cnt[d.comp[d.find(a - 1)]] -= 1
                cnt[d.comp[d.find(a)]] -= 1
                d.union(a - 1, a)
                cnt[d.comp[d.find(a)]] += 1

            if nums[a + 1]:
                cnt[d.comp[d.find(a + 1)]] -= 1
                cnt[d.comp[d.find(a)]] -= 1
                d.union(a, a + 1)
                cnt[d.comp[d.find(a)]] += 1

            nums[a] = True

            if cnt[m]:
                ret = index + 1

            #print(index, a, cnt)

        return ret
