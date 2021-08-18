
n, d = list(map(int, input().split()))

ts = list(map(int, input().split()))

x = d - (sum(ts) + (n - 1) * 10)

if x >= 0:
    print(2 * (n - 1) + x // 5)
else:
    print(-1)
