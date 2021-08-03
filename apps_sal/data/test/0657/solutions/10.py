a, b = [int(i) for i in input().split()]
x, y, z = [int(i) for i in input().split()]
ans = 0
if b - (z * 3 + y) < 0:
    ans += b - (z * 3 + y)
if a - (2 * x + y) < 0:
    ans += a - (2 * x + y)
print(abs(ans))
