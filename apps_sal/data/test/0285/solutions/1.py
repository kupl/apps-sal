n = int(input())
(x1, x2) = list(map(float, input().split()))
x1 += 1e-10
x2 -= 1e-10
lines = [tuple(map(float, input().split())) for _ in range(n)]
l1 = sorted(((k * x1 + b, i) for (i, (k, b)) in enumerate(lines)))
l2 = sorted(((k * x2 + b, i) for (i, (k, b)) in enumerate(lines)))
if [i for (x, i) in l1] == [i for (x, i) in l2]:
    print('NO')
else:
    print('YES')
