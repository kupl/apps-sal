class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.size = [0] * n
        self.groupCount = [0] * (n + 1)

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def add(self, x):
        self.size[x] = 1
        self.groupCount[1] += 1

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        self.groupCount[self.size[px]] -= 1
        self.groupCount[self.size[py]] -= 1
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.size[py] = 0
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.size[px] = 0
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.size[px] = 0
            self.rank[py] += 1
        self.groupCount[self.size[px]] += 1
        self.groupCount[self.size[py]] += 1
        return True

    def getSize(self, i):
        px = self.find(i)
        return self.size[px]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        disjoint = UnionFind(len(arr))
        ans = -1
        val = [0] * len(arr)
        for k in range(len(arr)):
            index = arr[k] - 1
            val[index] += 1
            disjoint.add(index)
            if index > 0 and val[index] == val[index - 1]:
                disjoint.union(index, index - 1)
            if index + 1 < len(val) and val[index] == val[index + 1]:
                disjoint.union(index, index + 1)
            if disjoint.groupCount[m] > 0:
                ans = k + 1
            '\n            i = 0\n            while i < len(arr):\n                if val[i] == 1 and disjoint.getSize(i) == m:\n                    i += disjoint.getSize(i)\n                    ans = k + 1\n                    continue\n                i += 1\n            '
        return ans
    '\n    def findLatestStep(self, arr: List[int], m: int) -> int:\n        def check(i):\n            val = [0]*len(arr)\n            for k in range(i+1):\n                val[arr[k]-1] = 1\n            count = 0\n            success = False\n            for k in range(len(val)):\n                if val[k] > 0:\n                    count += 1\n                else:\n                    if count == m:\n                        success = True\n                        break\n                    count = 0\n            if count == m:\n                success = True\n            return success                \n            \n        left = 0\n        right = len(arr)\n        while left < right:\n            mid = left + (right - left) //2\n            if not check(mid):\n                right = mid\n            else:\n                left = mid + 1\n        print(left)\n        if left == 0 and not check(left):\n            return -1\n        else:\n            return left\n    '
