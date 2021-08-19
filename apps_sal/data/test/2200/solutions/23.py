(n, a, b) = [int(c) for c in input().split()]
days = [int(c) for c in input().split()]
res = []
for i in range(len(days)):
    p = days[i] * a % b
    f1 = int(p // a)
    res.append(f1)
print(' '.join(map(str, res)))
