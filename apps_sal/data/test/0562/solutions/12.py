from math import inf
n = int(input())
a = []
for _ in range(n):
    b = list(map(int, input().split()))
    a.append(b)
a.sort()


def f(a):
    i = a[0]
    j = a[1]
    q = 2
    k = 0
    while 1:
        if a[q][0] == k:
            return 'NO'
        if i[1] == k:
            i = a[q]
            q += 1
        if len(a) == q:
            return 'YES'
        if j[1] == k:
            j = a[q]
            q += 1
        if len(a) == q:
            return 'YES'
        k = min(i[1], j[1], a[q][0])


if n <= 2:
    print('YES')
else:
    print(f(a))
