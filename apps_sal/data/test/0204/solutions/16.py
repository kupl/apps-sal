import fractions

a, b, x, y = list(map(int, input().split()))

d = fractions.gcd(x, y)
x //= d
y //= d
ans = min(a // x, b // y)
print(ans)

