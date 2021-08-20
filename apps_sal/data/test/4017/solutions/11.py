n = int(input())
a = [int(i) for i in input().split()]
b = sorted(a)
s = sum(b[:-1])
f = s - b[-1]
r = set()
if f > 0 and (not (b.count(f) == 1 and b[-1] == f)):
    for i in range(n):
        if a[i] == f:
            r.add(i + 1)
if sum(b[:-2]) == b[-2]:
    for i in range(n):
        if a[i] == b[-1]:
            r.add(i + 1)
print(len(r))
r = list(r)
print(' '.join((str(i) for i in r)))
