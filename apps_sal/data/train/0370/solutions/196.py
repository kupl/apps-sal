class UnionFind():
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [0] * n
    
    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        pi = self.find(i)
        pj = self.find(j)
        
        if pi != pj:
            self.parent[max(pi, pj)] = min(pi, pj)
            self.size[min(pi, pj)] += self.size[max(pi, pj)]
            self.size[max(pi, pj)] = 0 
            
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def decompose(num):
            if num == 1:
                return []
            res = []
            remain = num
            for factor in range(2, int(math.sqrt(num))+1):
                if remain % factor == 0:
                    while remain % factor == 0:
                        remain //= factor
                    res.append(factor)
            if remain > 1 and num % remain == 0:
                res.append(remain)
            return res
        
       
        unions = UnionFind(len(A))
        factor_index = collections.defaultdict(int)
        for idx, num in enumerate(A):
            factors = decompose(num)
            # print(\"factors\", factors)
            unions.size[idx] += 1
            for factor in factors:
                if factor not in factor_index:
                    factor_index[factor] = idx
                unions.union(factor_index[factor], idx)
                # print(\"factor\", factor, \"unions\", unions.parent, unions.size )
        return max(unions.size)
        
            
            

