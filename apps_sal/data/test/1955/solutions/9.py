from sys import stdin, stdout


def ri():
    return map(int, stdin.readline().split())


def solve(ee):
    dest = [-1 for i in range(m)]
    for i in range(ee, -1, -1):
        if d[i] != -1 and dest[d[i]] == -1:
            dest[d[i]] = i
    pd = -1
    for i in range(ee + 1):
        da = d[i]
        if da != -1 and dest[da] == i:
            pd += a[da]
            pd += 1
            if pd > i:
                return 0
    if dest.count(-1):
        return 0
    else:
        return 1


(n, m) = ri()
d = list(ri())
a = list(ri())
d = [i - 1 for i in d]
s = 0
e = n
while s < e:
    mid = (e + s) // 2
    if solve(mid):
        e = mid
    else:
        s = mid + 1
if s >= n:
    print(-1)
else:
    print(s + 1)
