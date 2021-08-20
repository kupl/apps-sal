from collections import namedtuple


def pairs(n):
    return n * (n - 1) / 2


n = int(input())
a = [int(s) for s in input().split()]
Q = namedtuple('Q', ['l', 'r'])
ql = []
m = int(input())
for i in range(m):
    (l, r) = [int(s) for s in input().split()]
    ql.append(Q(l, r))
p = 0
for i in range(n):
    for j in range(i + 1, n):
        if a[j] < a[i]:
            p += 1
ev = p % 2 == 0
for q in ql:
    s = q.r - q.l + 1
    if pairs(s) % 2 == 1:
        ev = not ev
    print('even' if ev else 'odd')
