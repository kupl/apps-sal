from collections import OrderedDict
n, d = map(int, input().split())

a = dict()
for _ in range(n):
    m, s = map(int, input().split())
    if m in a:
        a[m] += s
    else:
        a[m] = s

a = OrderedDict(sorted(a.items()))
a = [item for item in a.items()]

k = 0
su = 0
mu = 0
for i in range(len(a)):
    su += a[i][1]
    while a[i][0] - a[k][0] >= d:
        su -= a[k][1]
        k += 1
    mu = max(mu, su)

print(mu)
