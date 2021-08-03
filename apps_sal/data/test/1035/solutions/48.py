from math import gcd
a, b = map(int, input().split())
x = gcd(a, b)
cnt = 1
for i in range(2, int(x ** 0.5) + 1):
    if x == 1:
        break
    if x % i == 0:
        cnt += 1
        while x % i == 0:
            x //= i
else:
    if x != 1:
        cnt += 1
print(cnt)
