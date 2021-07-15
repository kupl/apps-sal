for test in range(int(input())):
    s = input()
    a = []
    now = 0
    n = len(s)
    for i in range(n):
        if s[i] == "0":
            if now > 0:
                a.append(now)
            now = 0
        else:
            now += 1
    if now > 0:
        a.append(now)
    a.sort(reverse=True)
    ans = 0
    for i in range(0, len(a), 2):
        ans += a[i]
    print(ans)
