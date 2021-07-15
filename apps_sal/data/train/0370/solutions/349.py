class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        A_max = max(A)
        primes = []
        seive = [True] * (int(sqrt(A_max)) + 1)
        seive[:2] = [False, False]
        for i in range(len(seive)):
            if seive[i]:
                primes.append(i)
                for j in range(i + i, len(seive), i):
                    seive[j] = False
        
        graph = defaultdict(list)
        for i, num in enumerate(A):
            for p in primes:
                if p * p > num:
                    
                    break
                if num % p  == 0:
                    while num % p == 0:
                        num //= p
                    graph[p].append(i)
            if num > 1:
                graph[num].append(i)
        print(graph)
        uf = DS(len(A))
        for indx in list(graph.values()):
            for i in range(1, len(indx)):
                uf.union(indx[i - 1], indx[i])
        parents = [uf.find(i) for i in range(len(A))]
        return max(Counter(parents).values())
                


class DS:
    def __init__(self, n):
        self.p = [-1]*n
    
    def find(self, x):
        if self.p[x] >= 0:
            self.p[x] = self.find(self.p[x])
            return self.p[x]
        return x
    
    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.p[x] < self.p[y]:
            self.p[x] -= 1
            self.p[y] = x

            
        else:
            self.p[y] -= 1
            self.p[x] = y
            
        
        

