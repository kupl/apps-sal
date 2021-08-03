class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        uf = [-1 for i in range(n + 1)]
        size = [0 for i in range(n + 1)]
        counts = [0 for i in range(n + 1)]
        fliped = set()

        res = -1
        for i in range(0, len(arr)):
            val = arr[i]
            uf[val] = val
            size[val] = 1
            counts[1] += 1
            fliped.add(val)
            if val - 1 in fliped:
                self.union(uf, val - 1, val, size, counts)
            if val + 1 in fliped:
                self.union(uf, val, val + 1, size, counts)
            if counts[m] > 0:
                res = max(res, i + 1)
        return res

    def root(self, uf: List[int], a: int) -> int:
        root = a
        while uf[root] != root:
            root = uf[root]

        next = a
        while next != root:
            next = uf[a]
            uf[a] = root
        return root

    def union(self, uf: List[int], a: int, b: int, size: List[int], counts: List[int]):
        roota = self.root(uf, a)
        rootb = self.root(uf, b)

        large = max(roota, rootb)
        small = min(roota, rootb)
        uf[large] = small
        counts[size[large]] -= 1
        counts[size[small]] -= 1

        size[small] = size[large] + size[small]
        counts[size[small]] += 1
