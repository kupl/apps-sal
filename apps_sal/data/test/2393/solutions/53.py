def zf(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = 0
    r = 0
    for i in range(1, n):
        if i <= r:
            z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z


t = int(input())
for i in range(t):
    s = input()
    ban1 = 'one'
    ban2 = 'two'
    ban21 = 'twone'
    s1 = ban1 + 'A' + s
    s2 = ban2 + 'A' + s
    s21 = ban21 + 'A' + s
    c = 0
    l = len(s)
    z1 = zf(s1)
    z2 = zf(s2)
    z21 = zf(s21)
    ans = []
    i = 0
    while i < l:
        if z21[i + 6] == 5:
            c += 1
            ans.append(i + 3)
            i += 5
            continue
        if z1[i + 4] == 3:
            c += 1
            ans.append(i + 2)
            i += 3
            continue
        if z2[i + 4] == 3:
            c += 1
            ans.append(i + 2)
            i += 3
            continue
        i += 1
    print(c)
    print(*ans)
