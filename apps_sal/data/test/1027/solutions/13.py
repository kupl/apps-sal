a = list(map(int, input().split()))
ans = 0
for i in range(14):
    ss = a[i]
    m = 0
    for j in range(1, 15):
        p = (i + j) % 14
        if ss == 0:
            if j != 14 and a[p] % 2 == 0:
                m += a[p]
            continue
        ns = ss // 14
        if ss % 14 != 0:
            ns += 1
        if j != 14 and (ns + a[p]) % 2 == 0:
            m += ns + a[p]
        elif j == 14 and ns % 2 == 0:
            m += ns
        ss -= 1
    ans = max(ans, m)
print(ans)
