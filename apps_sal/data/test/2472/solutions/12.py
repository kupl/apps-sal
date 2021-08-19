from operator import itemgetter
n = int(input())
l = []
for i in range(n):
    (a, b) = map(int, input().split())
    l.append([a, b])
l = sorted(l, key=itemgetter(1))
tmp = 0
f = 1
for (i, j) in l:
    tmp += i
    if tmp > j:
        f = 0


def Y(a, t=0):
    if a == t:
        print('YES')
    else:
        print('NO')


def y(a, t=0):
    if a == t:
        print('Yes')
    else:
        print('No')


y(f, 1)
