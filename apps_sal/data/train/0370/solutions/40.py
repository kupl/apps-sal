class DSU:
    def __init__(self):
        self.N = 0
        self.map = {}
        self.parent = []
        self.count = []

    def __contains__(self, obj):
        return obj in self.map

    def add(self, obj):
        if obj in self:
            return
        i = self.N
        self.N += 1
        self.map[obj] = i
        self.parent.append(i)
        self.count.append(0)

    def find(self, obj):
        p = self.parent

        origI = self.map[obj]

        i = origI
        while p[i] != i:
            i = p[i]
        root = i

        i = origI
        while p[i] != i:
            p[i], i = root, p[i]

        return root

    def union(self, objA, objB):
        rObjA = self.find(objA)
        rObjB = self.find(objB)
        if rObjA == rObjB:
            return
        self.count[rObjA] += self.count[rObjB]
        self.parent[rObjB] = rObjA

    def incCount(self, obj):
        rObj = self.find(obj)
        self.count[rObj] += 1
        return self.count[rObj]


class Solution:
    def largestComponentSize(self, nums) -> int:
        UF = DSU()
        max_ = 1
        for num in nums:
            if num == 1:
                continue
            pDs = self.primeDivisors(num)
            pD0 = pDs.pop()
            UF.add(pD0)
            for pD in pDs:
                UF.add(pD)
                UF.union(pD0, pD)
            count = UF.incCount(pD0)
            max_ = max(max_, count)
        return max_

    def primeDivisors(self, num: int):
        x = num

        pDs = set()

        if x % 2 == 0:
            pDs.add(2)
            while x % 2 == 0:
                x >>= 1

        if x % 3 == 0:
            pDs.add(3)
            while x % 3 == 0:
                x //= 3

        div = 5
        d2 = True
        while x >= div * div:
            if x % div == 0:
                pDs.add(div)
                while x % div == 0:
                    x //= div
            div += 2 if d2 else 4
            d2 = not d2

        if x > 1:
            pDs.add(x)

        return pDs
