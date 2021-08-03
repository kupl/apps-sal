n = int(input())
a = sorted((l, -r, i)for i, (l, r) in
           enumerate((map(int, input().split())for _ in [0] * n), 1))
print(*next(((y[2], x[2])for x, y in zip(a, a[1:])if x[1] <= y[1]), (-1, -1)))
