(N, Z, W) = map(int, input().split(' '))
a = list(map(int, input().split(' ')))
t1 = abs(a[N - 1] - W)
if N > 1:
    t2 = abs(a[N - 1 - 1] - a[N - 1])
else:
    t2 = 0
if N > 2:
    t3 = min(abs(a[N - 2 - 1] - a[N - 1]), abs(a[N - 1] - a[N - 1 - 1]))
else:
    t3 = 0
print(max(t1, t2, t3))
