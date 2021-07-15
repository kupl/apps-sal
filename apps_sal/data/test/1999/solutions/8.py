n = int(input())
a = list(map(int, input().split()))

c = {}

for p in range(len(a)):
    while c.get(a[p], -1) >= 0:
        a[c[a[p]]] = 0
        c[a[p]] = -1
        a[p] *= 2

    c[a[p]] = p

solution = [str(x) for x in a if x > 0]
print(len(solution))
print(' '.join(solution))
