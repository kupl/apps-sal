class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1]*(n+1)
        self.rnk = [0]*(n+1)

    def Find_Root(self, x):
        if(self.root[x] < 0):
            return x
        else:
            self.root[x] = self.Find_Root(self.root[x])
            return self.root[x]
    
    def Unite(self, x, y):
        x = self.Find_Root(x)
        y = self.Find_Root(y)
        if(x == y):
            return 
        elif(self.rnk[x] > self.rnk[y]):
            self.root[x] += self.root[y]
            self.root[y] = x

        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            if(self.rnk[x] == self.rnk[y]):
                self.rnk[y] += 1
    
    def isSameGroup(self, x, y):
        return self.Find_Root(x) == self.Find_Root(y)

    def Count(self, x):
        return -self.root[self.Find_Root(x)]


import sys
input = sys.stdin.readline
from bisect import bisect_right

N, M = map(int, input().split())
uni = UnionFind(N+1)
Edges = {}
for _ in range(N-1):
    a, b, w = map(int, input().split())
    if not w in Edges:
        Edges[w] = [(a, b)]
    else:
        Edges[w].append((a, b))

Query = list(map(int, input().split()))

Weights = sorted(list(Edges.keys()))

Score = [0]
score = 0
for w in Weights:
    for a, b in Edges[w]:
        c1 = uni.Count(a)
        c2 = uni.Count(b)
        c = c1 + c2
        score += c*(c-1)//2 - c1*(c1-1)//2 - c2*(c2-1)//2
        uni.Unite(a, b)
    Score.append(score)

ans = []
for q in Query:
    ind = bisect_right(Weights, q)
    ans.append(Score[ind])

print(*ans)
