from math import factorial
from collections import Counter


def cmb(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort(reverse=True)
l = Counter(v)

avg = 0
cnt = 0
for i in range(A, B + 1):
    tmp = sum(v[:i]) / i
    if tmp > avg:
        avg = tmp
        cnt = cmb(l[v[A - 1]], v[:i].count(v[i - 1]))
    elif tmp == avg:
        cnt += cmb(l[v[A - 1]], v[:i].count(v[i - 1]))
print(avg)
print(cnt)
