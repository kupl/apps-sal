import math
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = {}
for i in range(n):
    count = 0
    temp = a[i]
    while temp % 2 == 0:
        count += 1
        temp //= 2
    b.setdefault(count, 0)
    b[count] += 1
if len(b.keys()) >= 2:
    ans = 0
else:
    temp = 1
    for i in range(n):
        temp = temp * a[i] // math.gcd(temp, a[i])
    temp2 = temp // 2
    ans = m // temp2 - m // temp
print(ans)
