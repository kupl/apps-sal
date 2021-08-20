import sys
f = sys.stdin
f.readline()
a = sorted([int(x) for x in f.readline().split()])
b = [a[0]]
c = [True]
for i in range(1, len(a)):
    if a[i] != a[i - 1]:
        b.append(a[i])
    c.append(a[i] != a[i - 1])
for i in range(len(a) - 1, -1, -1):
    if a[i] < b[-1] and (not c[i]):
        b.append(a[i])
print(len(b))
for i in b:
    print(i, end=' ')
