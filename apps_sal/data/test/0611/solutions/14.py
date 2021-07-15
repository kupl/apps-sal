R = lambda: map(int, input().split())

n, m = R()

max_s = min_s = 0
t = (n + 1) // 2
for i in range(1, n+1):
    max_s += i - 1
    min_s += abs(i - t)

s = 0
for _ in range(m):
    x, d = map(int, input().split())
    if d > 0:
        s += n*x + d * max_s
    else:
        s += n*x + d * min_s
print('{:.8f}'.format(s / n))
