class dsu:

    def __init__(self, n):
        self.arr = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self.s = n

    def find(self, i):
        while i != self.arr[i]:
            i = self.arr[i]
        return i
        if self.arr[i] != i:
            self.arr[i] = self.find(self.arr[i])
        return self.arr[i]

    def union(self, i, j):
        fa = self.find(i)
        fb = self.find(j)
        if fa == fb:
            return
        s1 = self.size[fa]
        s2 = self.size[fb]
        if s1 < s2:
            self.arr[fa] = fb
            self.size[fb] += self.size[fa]
        else:
            self.arr[fb] = fa
            self.size[fa] += self.size[fb]


n = int(input())
zero = dsu(n)
one = dsu(n)
for i in range(n - 1):
    a = [int(i) for i in input().split(' ')]
    x = a[0] - 1
    y = a[1] - 1
    c = a[2]
    if c == 0:
        zero.union(x, y)
    else:
        one.union(x, y)
count = 0
for i in range(n):
    if zero.arr[i] == i:
        count += zero.size[i] * (zero.size[i] - 1)
    if one.arr[i] == i:
        count += one.size[i] * (one.size[i] - 1)
    count += (zero.size[zero.find(i)] - 1) * (one.size[one.find(i)] - 1)
print(count)
