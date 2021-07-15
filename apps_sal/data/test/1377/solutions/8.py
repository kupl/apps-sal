n = int(input())
l = list(map(int, input().split()))
to = l.index(max(l))
ok = 1
for i in range(1, to):
    if (l[i] <= l[i - 1]):
        ok = 0
        break
for i in range(to + 1, n):
    if (l[i] >= l[i - 1]):
        ok = 0
        break
if ok:
    print('YES')
else:
    print('NO')
