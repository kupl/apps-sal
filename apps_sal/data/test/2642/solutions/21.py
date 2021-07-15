from math import gcd
mod = 1000000007
n = int(input())
zero = 0
bad = {}
for i in range(n):
    x, y = list(map(int, input().split()))
    if x == 0 and y == 0:
        zero += 1
        continue
    g = gcd(x, y)
    x //= g
    y //= g
    if y < 0: x, y = -x, -y
    if y==0 and x<0: x, y = -x, -y
    is_rotate90 = (x <= 0)
    if is_rotate90: x, y = y, -x
    if not (x, y) in bad: bad[x, y] = [0, 0]
    bad[x, y][is_rotate90] += 1

ans = 1
for x, y in bad:
    c1, c2 = bad[x, y]
    c3 = (pow(2, c1, mod) - 1) + (pow(2, c2, mod) - 1) + 1
    ans *= c3
    ans %= mod

ans += zero - 1
ans = (ans + mod) % mod
print(ans)

