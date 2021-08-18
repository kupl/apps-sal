import math
n = int(input())
a = list(map(int, input().split()))
a.sort()
lr = [0] * n
rl = [0] * n

for i in range(n):
    if i == 0:
        g = a[0]
        lr[0] = g
    else:
        g = math.gcd(a[i], g)
        lr[i] = g

for i in range(n - 1, 0, -1):
    if n - 1 == i:
        g = a[n - 1]
        rl[n - 1] = g
    else:
        g = math.gcd(a[i], g)
        rl[i] = g
hantei = 0
ans = 0
for i in range(n):
    if i == 0:
        hantei = rl[1]
    elif i == n - 1:
        hantei = lr[n - 2]
    else:
        hantei = math.gcd(lr[i - 1], rl[i + 1])
    if ans <= hantei:
        ans = hantei

print(ans)
