n, k, q = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 10000000000000
for m in a:
    res = []
    l = []
    for x in a:
        if x < m and l:
            if len(l) >= k:
                l.sort()
                for p in l[:len(l) - k + 1]:
                    res.append(p)
            l = []
        elif x >= m:
            l.append(x)
    if l:
        if len(l) >= k:
            l.sort()
            for p in l[:len(l) - k + 1]:
                res.append(p)
    res.sort()
    if len(res) >= q:
        ans = min(ans, res[q - 1] - m)
if ans == 10000000000000:
    print((-1))
else:
    print(ans)

