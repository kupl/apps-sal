def mi():
    return list(map(int, input().split()))


'\n7\n5 5 4 5 5 5 6\n'
n = int(input())
a = list(mi())
od = 0
ev = 0
for i in range(n):
    if i % 2:
        od += a[i]
    else:
        ev += a[i]
cnt = 0
(rod, rev) = (0, 0)
for i in range(n - 1, -1, -1):
    if i % 2 == 0:
        ev -= a[i]
    else:
        od -= a[i]
    if ev + rev == od + rod:
        cnt += 1
    if i % 2 == 0:
        rod += a[i]
    else:
        rev += a[i]
print(cnt)
