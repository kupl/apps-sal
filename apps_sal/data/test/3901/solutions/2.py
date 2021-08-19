from math import gcd

n = int(input())
a = list(map(int, input().split()))

d = n
i = -1
v = a[0]

for j in range(n):
    # forward
    v = gcd(v, a[j])
    if v == 1:
        v = a[j]
        # backward
        for k in range(j, i, -1):
            v1 = gcd(v, a[k])
            if v1 == 1:
                d = min(d, j - k)
                i = k
                break
            v = v1

if d == 0:
    ans = n - a.count(1)
elif d < n:
    ans = d - 1 + n - a.count(1)
else:
    ans = -1

print(ans)
