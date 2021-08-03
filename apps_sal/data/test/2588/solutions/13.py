for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    s = input()
    if s == "0" * n:
        print(a * n + b * n + b)
        continue
    ans = 0
    ind = 0
    ind2 = n - 1
    pref = 0
    suf = 0
    while ind2 >= 0 and s[ind2] == "0":
        ind2 -= 1
        suf += 1
    while ind < n and s[ind] == "0":
        ind += 1
        pref += 1
    while ind <= ind2:
        if s[ind] == "0":
            size = 0
            while ind <= ind2 and s[ind] == "0":
                ind += 1
                size += 1
            ans += min((size - 1) * b + size * a + 2 * a, size * a + 2 * b * (size - 1))
        else:
            size = 0
            while ind <= ind2 and s[ind] == "1":
                ind += 1
                size += 1
            ans += (size + 1) * b * 2 + size * a
    ans += pref * b + pref * a + a
    ans += suf * b + suf * a + a
    print(ans)
