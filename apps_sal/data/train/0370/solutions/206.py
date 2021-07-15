class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = n
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        
        if xp == yp:
            return False
        if self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        elif self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        else:
            self.parent[xp] = yp
            self.rank[yp] += 1
        self.size -= 1
        return True
    def getSize(self):
        return self.size
    
class Solution:
    # refer submission. https://www.cnblogs.com/grandyang/p/13253468.html
    def largestComponentSize(self, A: List[int]) -> int:
        def getFactors(n):
            res = set()
            for i in range(2, int(sqrt(n)) + 2):
                if not n % i:
                    # don't count 1 in factor. e.g. [1,2,3,4,5,6,7,8,9]
                    for j in [i, n // i]:
                        if j != 1:
                            res.add(j)
            # prime number.
            if not res:
                return {n}
            return res
        
        # buld dsu based on index of A. union index.
        dsu = DSU(len(A) + 1)
        factor2Index = {}
        for i, n in enumerate(A):
            for factor in getFactors(n):
                if factor in factor2Index:
                    dsu.union(i, factor2Index[factor])
                factor2Index[factor] = i
        groupSize = collections.defaultdict(int)
        for i in range(len(A)):
            groupSize[dsu.find(i)] += 1
        return max(groupSize.values())
        

