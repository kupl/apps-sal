n = int(input())
a = sorted(((l, -r, i) for (l, r, i) in (map(int, input().split() + [i + 1]) for i in range(n))))
print(*next(((y[2], x[2]) for (x, y) in zip(a, a[1:]) if x[1] <= y[1]), (-1, -1)))
