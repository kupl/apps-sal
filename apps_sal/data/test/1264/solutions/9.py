import sys
f = sys.stdin
n = int(f.readline())
a = []
for s in f.readline().split():
    a += [int(s)]
m = 0
for i in range(n):
    for j in range(i, n):
        s1 = sum(a[:i])
        s2 = sum(1 - t for t in a[i:j + 1])
        s3 = sum(a[j + 1:])
        m = max(m, s1 + s2 + s3)
print(m)
