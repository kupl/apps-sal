N = int(input())
ret = 0
for i in range(N):
    ret += (i + 1) * (N - i)
for _ in range(N - 1):
    (x, y) = map(int, input().split())
    x -= 1
    y -= 1
    if x > y:
        (x, y) = (y, x)
    ret -= (x + 1) * (N - y)
print(ret)
