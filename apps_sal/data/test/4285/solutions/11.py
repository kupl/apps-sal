# for _ in range(int(input())):
for _ in range(1):
    n = int(input())
    s = input()
    suf = [0] * n
    suf[n - 1] = int(s[-1] in 'c')
    suf1 = [0] * n
    suf1[n - 1] = int(s[-1] in '?')
    mod = 10**9 + 7
    m = s.count('?')
    tr0 = pow(3, m, mod)
    if m - 1 >= 0:
        tr1 = pow(3, m - 1, mod)
    else:
        tr1 = 0
    if m - 2 >= 0:
        tr2 = pow(3, m - 2, mod)
    else:
        tr2 = 0
    trob = pow(3, mod - 2, mod)
    for i in range(n - 2, -1, -1):
        suf[i] = suf[i + 1] + int(s[i] in 'c')
        suf1[i] = suf1[i + 1] + int(s[i] in '?')
    for i in range(0, n - 1):
        if s[i] not in 'b?':
            suf[i + 1] = 0
            suf1[i + 1] = 0
        if s[i] == '?':
            suf[i + 1] *= tr1
            suf1[i + 1] *= tr2
            suf[i + 1] %= mod
            suf1[i + 1] %= mod
        else:
            suf[i + 1] *= tr0
            suf[i + 1] %= mod
            suf1[i + 1] *= tr1
            suf1[i + 1] %= mod
    suf[0] = 0
    suf1[0] = 0
    ans = 0
    kek = 0
    for i in range(n - 2, -1, -1):
        if s[i] not in 'a?':
            kek += suf[i + 1]
            kek += suf1[i + 1]
            continue
        if s[i] in 'a':
            ans += kek
        else:
            lol = kek * trob % mod
            ans += lol
        kek += suf[i + 1]
        kek += suf1[i + 1]
        ans %= mod
    print(ans)
