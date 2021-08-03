n, m = list(map(int, input().split()))
a = [int(x) for x in input().split()]
b = sorted([int(x) for x in input().split()])
lo = b[0]
hi = b[-1]
c = []

for k in range(len(a)):
    best = -1000000000000000001
    for i in range(len(a)):
        if i != k:
            best = max([best, a[i] * lo, a[i] * hi])
    c.append(best)
print(min(c))
