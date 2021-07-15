from collections import defaultdict, Counter
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        parent_x, parent_y = self.find(x), self.find(y)
        self.parent[parent_x] = parent_y
    
class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        
        def prime(num):
            i = 2
            temp = []
            while num >= i*i:
                if num % i == 0:
                    temp.append(i)
                    num = num//i
                else:
                    i += 1
            temp.append(num)
            return set(temp)
        
        dsu = DSU(len(A))
        graph = defaultdict(list)
        
        for i, num in enumerate(A):
            pr_set = prime(num)
            for q in pr_set: 
                graph[q].append(i)

        for _, indexes in list(graph.items()):
            for i in range(len(indexes)-1):
                dsu.union(indexes[i], indexes[i+1])

        return max(Counter([dsu.find(i) for i in range(len(A))]).values())

