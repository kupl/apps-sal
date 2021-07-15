n = int(input())
a = {}
for _ in range(n):
    aa, xx = [int(v) for v in input().split()]
    a[aa] = xx

m = int(input())
b = {}
for _ in range(m):
    bb, yy = [int(v) for v in input().split()]
    b[bb] = yy

sa = set(a.keys())
sb = set(b.keys())
both = sa & sb

print(
    sum(max(a[v], b[v]) for v in both) +
    sum(a[v] for v in sa - both) +
    sum(b[v] for v in sb - both)
)
