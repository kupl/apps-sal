n, m = map(int, input().split())
x = n // 2 + n % 2
while x <= n and x % m != 0:
    x += 1
if x > n:
    print(-1)
else:
    print(x)
