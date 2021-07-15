class UnionFind:
 
    def __init__(self, n):
        self.follow = [-1]*(n+1)
        self.num_follower = [1]*(n+1)
 
    def root_index_of(self, a):
        r = a
        while self.follow[r] > -1:
                 r = self.follow[r]
        return r
 
    def connected(self, a, b):
        return self.root_index_of(a) == self.root_index_of(b)
 
    def connect(self, a, b):
        ra = self.root_index_of(a)
        rb = self.root_index_of(b)
 
        if ra == rb:
            return
 
        if self.num_follower[ra] < self.num_follower[rb]:
            self.follow[ra] = rb
            self.follow[a] = rb
            self.num_follower[rb] += self.num_follower[ra]
        else:
            self.follow[rb] = ra
            self.follow[b] = ra
            self.num_follower[ra] += self.num_follower[rb]

import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
s = [input() for _ in range(n)]

uf = UnionFind(n+m)
v = [[] for _ in range(n+m)]
c = [0]*(n+m)
for i in range(n):
    for j in range(m):
        if s[i][j] == "=":
            uf.connect(i, j+n)

for i in range(n):
    for j in range(m):
        if s[i][j] == "<":
            v[uf.root_index_of(i)].append(uf.root_index_of(n+j))
            c[uf.root_index_of(n+j)] += 1
        elif s[i][j] == ">":
            v[uf.root_index_of(n+j)].append(uf.root_index_of(i))
            c[uf.root_index_of(i)] += 1


ans = [0]*(n+m)
used = [0]*(n+m)
que = deque([])
for i in range(n+m):
    if c[i] == 0:
        ans[i] = 1
        used[i] = 1
        que.append(i)


while que:
    x = que.popleft()
    for i in v[x]:
        if used[i]:
            continue
        ans[i] = max(ans[x]+1, ans[i])
        c[i] -= 1
        if c[i] == 0:
            used[i] = 1
            que.append(i)

for i in range(n+m):
    if used[i] == 0:
        print("No")
        return

for i in range(n):
    for j in range(m):
        if s[i][j] == "=":
            if ans[uf.root_index_of(i)] != ans[uf.root_index_of(n+j)]:
                print("No")
                return

for i in range(n):
    for j in range(m):
        if s[i][j] == "<":
            if ans[uf.root_index_of(i)] >= ans[uf.root_index_of(n+j)]:
                print("No")
                return

for i in range(n):
    for j in range(m):
        if s[i][j] == ">":
            if ans[uf.root_index_of(i)] <= ans[uf.root_index_of(n+j)]:
                print("No")
                return

print("Yes")
for i in range(n):
    print(ans[uf.root_index_of(i)], end=" ")
print()
for j in range(m):
    print(ans[uf.root_index_of(j+n)], end=" ")
print()


