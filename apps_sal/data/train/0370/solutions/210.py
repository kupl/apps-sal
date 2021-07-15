class DSU():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
        self.size = n
    def find(self, x):
        # print('x = {0}, parent = {1}, self.parent[x] = {2}, cond = {3}'.format(x, self.parent, self.parent[x], x != self.parent[x]))
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xp, yp = self.find(x), self.find(y)
        
        if xp == yp:
            return False
        # print('union, xp = {0}, yp = {1}'.format(xp, yp))
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
    def largestComponentSize(self, A: List[int]) -> int:
        def getFactors(n):
            res = set()
            for i in range(2, int(sqrt(n)) + 2):
                if not n % i:
                    # don't count 1 in factor. e.g. [1,2,3,4,5,6,7,8,9]
                    for j in [i, n // i]:
                        if j != 1:
                            res.add(j)
                    # res.add(n // i)
            # prime number.
            if not res:
                return {n}
            return res
        
        dsu = DSU(len(A) + 1)
        factor2Index = {}
        for i, n in enumerate(A):
            # print('factor2Index = {0}, n = {1}, factors = {2}'.format(factor2Index, n, getFactors(n)))
            for factor in getFactors(n):
                if factor in factor2Index:
                    # print('factor = {0}, i = {1}, other = {2}'.format(factor, i, factor2Index[factor]))
                    dsu.union(i, factor2Index[factor])
                factor2Index[factor] = i
        groupSize = collections.defaultdict(int)
        for i in range(len(A)):
            groupSize[dsu.find(i)] += 1
        return max(groupSize.values())
        

