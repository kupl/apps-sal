def check(mid):
    ans = []
    res = 0
    for c, count in d:
        tmp = count // mid
        if (count % mid != 0):
            tmp += 1
        ans.append((c, tmp))
        res += tmp
    return res <= n, ans


a = input()
n = int(input())
d = dict()
t = 0
for i in a:
    if i not in d:
        d[i] = 1
        t += 1
    else:
        d[i] += 1
ans = []
res = ""
for i in d:
    ans.append(i)
    res = i
if n >= len(a):
    print(1)
    print(a, end='')
    n -= len(a)
    for u in range(n):
        print(res, end='')
else:
    d = (sorted(d.items(), key=lambda d: (d[1], d[0])))
    l = 1
    r = len(a)
    res = []
    count_res = 0
    while (l <= r):
        mid = (l + r) // 2
        flag, tmp = check(mid)
        if (flag):
            r = mid - 1
            count_res = mid
            res = tmp
        else:
            l = mid + 1
    if (len(res) == 0):
        print(-1)
    else:
        ttt = 0
        print(count_res)
        for c, sl in res:
            for j in range(sl):
                print(c, end='')
                ttt += 1
        n -= ttt
        for i in range(n):
            print(a[0], end='')
