t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = []
    p = []
    cnt0 = 0
    for val in a:
        if val > 0:
            p.append(val)
        elif val < 0:
            m.append(val)
        else:
            cnt0 += 1
    p = sorted(p, reverse=True)
    m = sorted(m)
    ans = -10 ** 20
    tmp = 1
    if len(p) >= 5:
        for i in range(5):
            tmp *= p[i]
        ans = max(tmp, ans)
    tmp = 1
    if len(p) >= 4 and len(m) >= 1:
        for i in range(4):
            tmp *= p[~i]
        for i in range(1):
            tmp *= m[~i]
        ans = max(tmp, ans)
    tmp = 1
    if len(p) >= 3 and len(m) >= 2:
        for i in range(3):
            tmp *= p[i]
        for i in range(2):
            tmp *= m[i]
        ans = max(tmp, ans)
    tmp = 1
    if len(p) >= 2 and len(m) >= 3:
        for i in range(2):
            tmp *= p[~i]
        for i in range(3):
            tmp *= m[~i]
        ans = max(tmp, ans)
    tmp = 1
    if len(p) >= 1 and len(m) >= 4:
        for i in range(1):
            tmp *= p[i]
        for i in range(4):
            tmp *= m[i]
        ans = max(tmp, ans)
    tmp = 1
    if len(m) >= 5:
        for i in range(5):
            tmp *= m[~i]
        ans = max(tmp, ans)
    if cnt0 > 0:
        ans = max(0, ans)
    print(ans)
