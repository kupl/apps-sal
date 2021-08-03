import math

l, r, x, y = list(map(int, input().split()))

m = x * y

if l % x == 0:
    low = l
else:
    low = (l // x + 1) * x

cnt = 0
b = min(int(math.sqrt(m)), r)
while low <= b:
    if m % low == 0 and m // low <= r and math.gcd(low, m // low) == x:
        # print(low)
        cnt += 2
    low += x

b = int(math.sqrt(m))
if b >= l and b <= r and b * b == m and math.gcd(b, b) == x:
    cnt -= 1

print(cnt)
