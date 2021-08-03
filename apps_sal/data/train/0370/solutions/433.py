import collections


class DisjointSet:
    def __init__(self):
        self.size = {}
        self.parent = {}

    def makeSet(self, val):
        self.parent[val] = val
        self.size[val] = 1

    def find(self, val):
        if self.parent[val] == val:
            return val
        self.parent[val] = self.find(self.parent[val])
        return self.parent[val]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return self.size[x]
        if self.size[x] < self.size[y]:
            x, y = y, x

        self.parent[y] = x
        self.size[x] += self.size[y]
        return self.size[x]


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        A.sort()
        disjointSet = DisjointSet()
        for val in A:
            disjointSet.makeSet(val)
        factors = collections.defaultdict(set)
        ans = 0
        # print(disjointSet.size,disjointSet.parent)
        for val in A:
            for i in range(1, int(val**0.5) + 1):
                if i == 1:
                    # if val in factors:
                    #     ans=max(ans,disjointSet.union(factors[val],val))
                    # factors[val]=val
                    factors[val].add(val)
                    continue
                if val % i != 0:
                    continue
                factors[i].add(val)
                factors[val // i].add(val)
                # if i in factors:
                #     res=disjointSet.union(factors[i],val)
                #     # print(res,factors[i],val)
                #     ans=max(ans,res)
                # factors[i]=val
                # tmp=val//i
                # if tmp in factors:
                #     res=disjointSet.union(factors[tmp],val)
                #     # print(res,factors[tmp],val)
                #     ans=max(ans,res)
                # factors[tmp]=val
        # print(factors,disjointSet.parent,disjointSet.size)
        for _, itms in list(factors.items()):
            items = list(itms)
            i = 1
            while i < len(items):
                ans = max(ans, disjointSet.union(items[i - 1], items[i]))
                i += 1

        return ans
