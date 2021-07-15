p, k = list(map(int, input().split()))

ans = None
for x in range(0, k):
    res = []
    a = p
    used = set()
    ok = 1
    while 1:
        b = (-a+k-1) // k
        if b == 0:
            res.append(a)
            break
        res.append(a+k*b)
        a = b
        if a in used:
            ok = 0
            break
        used.add(a)
    if ok:
        ans = res
        break
if ans is None:
    print(-1)
else:
    print(len(ans))
    print(*ans)

