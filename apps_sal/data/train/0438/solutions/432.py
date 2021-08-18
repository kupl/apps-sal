class union(object):
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [0] * n
        self.count = collections.defaultdict(int)

    def find(self, p):
        if self.parent[p] == -1:
            return -1
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        if self.find(p) != self.find(q):
            pr = self.find(p)
            qr = self.find(q)

            self.count[self.size[pr]] -= 1
            self.count[self.size[qr]] -= 1
            self.parent[pr] = qr
            self.size[qr] += self.size[pr]
            self.count[self.size[qr]] += 1

    def add(self, p):
        self.parent[p] = p
        self.size[p] = 1
        self.count[1] += 1

    def get_size(self, m):

        return self.count[m] > 0


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr):
            return m
        uds = union(len(arr) + 1)
        ans = -1
        for i in range(len(arr)):
            uds.add(arr[i])
            if arr[i] + 1 <= len(arr) and uds.find(arr[i] + 1) != -1:
                uds.union(arr[i], arr[i] + 1)
            if arr[i] - 1 >= 1 and uds.find(arr[i] - 1) != -1:
                uds.union(arr[i] - 1, arr[i])
            if uds.get_size(m):
                ans = i + 1

        return ans
