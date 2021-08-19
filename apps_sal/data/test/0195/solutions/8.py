(a, b, c, n) = map(int, input().strip().split(' '))
if a + b - c >= n or a >= n or b >= n or (c >= n):
    print(-1)
elif c > min(a, b):
    print(-1)
else:
    print(n - a - b + c)
