import math
__author__ = 'PrimuS'

s = input()
n = len(s)

a = [0] * n
ps = [0] * n

for i in range(n):
    if s[i] in "IEAOUY":
        a[i] = 1

ps[0] = a[0]
for i in range(1, n):
    ps[i] = ps[i - 1] + a[i]

up = math.ceil((n - 1) / 2)
ss = [0] * up
prev = 0
for i in range(up):
    ss[i] = (a[i] + a[n - i - 1]) * (i + 1)
    if i == n - i - 1:
        ss[i] /= 2
    ss[i] += prev
    prev = ss[i]


res = 0
x = 0
res = ps[n - 1]
for i in range(2, n):
    k = n - i + 1
    cur = 0
    if k < i:
        cur += (ps[n - k] - ps[k - 2]) * k
        cur += ss[k - 2]
    else:
        cur += (ps[n - i] - ps[i - 2]) * i
        cur += ss[i - 2]

    res += cur / i

if n > 1:
    res += ps[n - 1] / n

print(res)
