class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size

    def find(self, value):
        if value == self.parent[value]:
            return value
        self.parent[value] = self.find(self.parent[value])
        return self.parent[value]

    def merge(self, value1, value2):
        p1, p2 = self.parent[value1], self.parent[value2]
        if p1 == p2:
            return
        self.parent[p1] = p2
        self.size[p2] += self.size[p1]


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        c = Counter()
        d = DSU(n + 2)
        vis = [0] * (n + 2)
        answer = -1
        for i in range(n):
            c[1] += 1
            vis[arr[i]] = 1
            if vis[arr[i] - 1] and d.find(arr[i]) != d.find(arr[i] - 1):
                c[d.size[d.find(arr[i])]] -= 1
                c[d.size[d.find(arr[i] - 1)]] -= 1
                d.merge(arr[i], arr[i] - 1)
                c[d.size[d.find(arr[i])]] += 1
            if vis[arr[i] + 1] and d.find(arr[i]) != d.find(arr[i] + 1):
                c[d.size[d.find(arr[i])]] -= 1
                c[d.size[d.find(arr[i] + 1)]] -= 1
                d.merge(arr[i], arr[i] + 1)
                c[d.size[d.find(arr[i])]] += 1
            if c[m] > 0:
                answer = i + 1
        return answer
