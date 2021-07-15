import math
import functools
from collections import defaultdict

n, m = map(int, input().split(' '))

v = [i for i in map(int, input().split(' '))]

s = [0 for i in range(n + 2)]

for i in range(m - 1):
    if abs(v[i] - v[i + 1]) < 2:
        continue
    s[min(v[i], v[i + 1]) + 1] += 1
    s[max(v[i], v[i + 1])] -= 1

p = 0

for i in range(m - 1):
    p += abs(v[i] - v[i + 1])

ans = [0 for i in range(n + 2)]

d = 0

for i in range(n + 2):
    d += s[i]
    ans[i] = d

a = defaultdict(lambda : 0, {})
b = defaultdict(lambda : [], {})

for i in range(m - 1):
    if v[i] == v[i + 1]:
        continue
    a[min(v[i], v[i + 1])] += 1
    b[max(v[i], v[i + 1])].append(min(v[i], v[i + 1]))

for i in range(1, n + 1):
    q = p
    q = ans[i]
    q = a[i] * (i - 1)
    q = len(b[i]) * i
    q = 2 * sum(b[i])
    print(p -
          ans[i] +
          a[i] * (i - 1) -
          len(b[i]) * i +
          2 * sum(b[i]), end=' ')
