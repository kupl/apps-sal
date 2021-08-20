import math
from sys import stdin, stdout


def input():
    return stdin.readline()[:-1]


class disjoint_set:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def union(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)
        if p1 == p2:
            return False
        if self.size[p1] > self.size[p2]:
            self.parent[p2] = p1
            self.size[p1] += self.size[p2]
        else:
            self.parent[p1] = p2
            self.size[p2] += self.size[p1]

    def find(self, x):
        ans = x
        while ans != self.parent[ans]:
            ans = self.parent[ans]
        temp = x
        while temp != self.parent[temp]:
            temp2 = self.parent[temp]
            self.parent[temp] = ans
            temp = temp2
        return ans


(n, m) = map(int, input().split())
ds = disjoint_set(n)
for i in range(m):
    l = list(map(int, input().split()))
    for i in range(2, l[0] + 1):
        ds.union(l[i - 1] - 1, l[i] - 1)
for i in range(n):
    print(ds.size[ds.find(i)], end=' ')
print('')
