class UF(object):
    def uf(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n
        
    def find(self, x):
        if x != self.uf[x]:
            self.uf[x] = self.find(self.uf[x])
        return self.uf[x]

    def union(self, x, y):
        xx = self.find(x)
        yy = self.find(y)
        if xx == yy:
            return 
        self.uf[xx] = yy
        self.size[yy] += self.size[xx]
        # self.size[xx] = 0
        
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def primefactors(n):
            # 暴力求取因子
            out = set()
            # 第一步是提取2且n变成奇数
            while n % 2 == 0:
                out.add(2)
                n //= 2
            # 第二步是从3开始遍历奇数
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    out.add(i)
                    n //= i
            # 第三步关照额外corner情况
            if n > 2:
                out.add(n)
            return out
        '''
        idx_lookup = {A[i] : i for i in range(len(A))} 
        uf = UF()
        uf.uf(len(A))
        # 使用因子作为key 来收集index表示公有相同因子
        primeAndItsMultiples = collections.defaultdict(list)
        for i in A:
            factors = primefactors(i)
            for f in factors:
                primeAndItsMultiples[f].append(i)
        for idx, multiples in primeAndItsMultiples.items():
            if multiples:
                root = multiples[0] # use the first multiple as their root
                for node in multiples[1:]:
                    uf.union(idx_lookup[node], idx_lookup[root]) # connect node with root             
        return max(uf.size)
        '''
        uf = UF()
        uf.uf(len(A))
        
        prime = {}
        for i, v in enumerate(A):
            factors = primefactors(v)
            for p in factors:
                if p in prime:
                    uf.union(i, prime[p])
                else:
                    prime[p] = i
        return max(uf.size)
