from math import gcd
m, a, b = list(map(int, input().split()))
last, x = 0, gcd(a, b)
s = [1] * (a + b + 1)
q1, ans = 0, 1
max1, s[0] = [[0, 1]], 0
while q1 < a + b:
    if q1 > b and s[q1 - b]:
        ans += 1
        q1 -= b
        s[q1] = 0
    else:
        q1 += a
        if q1 > last:
            max1.append([q1, ans])
            last = q1
        if s[q1]:
            ans += 1
            s[q1] = 0
ans1 = q1 = 0
for q in range(min(m + 1, a + b)):
    if max1[q1 + 1][0] == q:
        q1 += 1
    ans1 += max1[q1 + 1][1]
if m >= a + b:
    ans1 += (m // x + 1) * (m % x + 1)
    m -= m % x + 1
    p, t = (a + b) // x, (m - a - b) // x
    ans1 += (t + 1) * (t + 2) // 2 * x
    ans1 += p * (t + 1) * x
print(ans1)
