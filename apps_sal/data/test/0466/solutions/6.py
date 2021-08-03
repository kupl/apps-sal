def readln(): return tuple(map(int, input().split()))


c, d = readln()
n, m = readln()
k, = readln()

ans = 1 << 30
for x in range(10001):
    y = max(0, n * m - k - n * x)
    if y >= 0 and ans > c * x + d * y:
        ans = c * x + d * y
print(ans)
