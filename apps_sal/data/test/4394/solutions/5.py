class DisjoinSet:
    def __init__(self, n):
        self.n = n
        self.dad = [i for i in range(n + 1)]
        self.cant = [1] * (n + 1)

    def SetOf(self, n):
        if self.dad[n] == n:
            return n
        self.dad[n] = self.SetOf(self.dad[n])
        return self.dad[n]

    def Merge(self, a, b):
        a, b = self.SetOf(a), self.SetOf(b)
        if a != b:
            if self.cant[b] > self.cant[a]:
                a, b = b, a
            self.cant[a] += self.cant[b]
            self.dad[b] = a
            return True
        return False


def Kruskal(l, n):
    l.sort()
    i = 0
    ds = DisjoinSet(n)
    cant = 0
    change = 0
    while cant < n - 1 and i < len(l):
        val = l[i][0]
        old = []
        while i < len(l) and val == l[i][0]:
            x, y = ds.SetOf(l[i][1]), ds.SetOf(l[i][2])
            if x != y:
                old.append((x, y))
            i += 1
        change += len(old)
        for (x, y) in old:
            change -= ds.Merge(x, y)
    return change


n, m = input().split()
n, m = int(n), int(m)

e = []
for i in range(m):
    x, y, c = input().split()
    e.append((int(c), int(x), int(y)))

print(Kruskal(e, n))

