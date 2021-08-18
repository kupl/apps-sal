def check(now):
    last = [0 for i in range(0, m + 1)]
    ddl = []
    last[0] = -1
    for i in range(now, 0, -1):
        if last[d[i]] == 0:
            ddl.append(d[i])
            last[d[i]] = i
    day = 0
    if len(ddl) != m:
        return False
    for i in range(1, m + 1):
        day += a[ddl[-i]]
        if day >= last[ddl[-i]]:
            return False
        day += 1
    return True


a = input()
a = a.split()
n = int(a[0])
m = int(a[1])
d = input()
d = d.split()
a = input()
a = a.split()
a = [0] + a
d = [0] + d
for i in range(0, n + 1):
    d[i] = int(d[i])
for i in range(0, m + 1):
    a[i] = int(a[i])
l = 0
r = n + 1
while l < r - 1:
    mid = (l + r) >> 1
    if check(mid):
        r = mid
    else:
        l = mid
if r == n + 1:
    print(-1)
else:
    print(r)
