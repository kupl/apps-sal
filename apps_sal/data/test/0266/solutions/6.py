def find(step):
    if m == 1 and s == 0:
        return 0
    ss = s
    res = ''
    for i in range(m):
        j = 1 if i == 0 else 0
        ok = False
        c = list(range(j, 10)) if step == -1 else reversed(list(range(j, 10)))
        for v in c:
            if 0 <= ss - v <= (m - i - 1) * 9:
                ok = True
                ss -= v
                res += str(v)
                break
        if not ok:
            return -1
    return res


m, s = list(map(int, input().split()))
print(find(-1), find(1))
