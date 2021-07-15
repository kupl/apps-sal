class Solution:
    def find(self, parent: List[int], x: int):
        if not parent[x] == x:
            parent[x] = self.find(parent, parent[x])
        return parent[x]
    
    def largestComponentSize(self, A: List[int]) -> int:
        n, mx, res = 0, max(A), 0
        valtocnt = collections.Counter()
        parent = list(range(mx+1))  
        for num in A:
            for d in range(int(sqrt(num)), 1, -1):
                if num % d == 0:
                    parent[self.find(parent, num)] = parent[self.find(parent, d)]
                    parent[self.find(parent, num)] = parent[self.find(parent, num//d)]
        for num in A:
            valtocnt[self.find(parent, num)] += 1
            res = max(res, valtocnt[self.find(parent, num)])
        return res
