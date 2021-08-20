tt = int(input())
while tt > 0:
    tt -= 1
    s = input()
    n = len(s)
    (o, t, r) = ([0] * n, [0] * n, [0] * n)
    o[0] = t[0] = r[0] = -1
    ans = n + 1
    for i in range(n):
        if i > 0:
            o[i] = o[i - 1]
            t[i] = t[i - 1]
            r[i] = r[i - 1]
        if s[i] == '1':
            o[i] = i
        elif s[i] == '2':
            t[i] = i
        else:
            r[i] = i
        mn = min(o[i], t[i], r[i])
        if mn > -1:
            ans = min(ans, i - mn + 1)
    if ans == n + 1:
        ans = 0
    print(ans)
