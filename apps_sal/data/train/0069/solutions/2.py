for i in range(int(input())):
    a, b = list(map(int, input().split()))
    s = input()
    j = 0
    n = len(s)
    l = []
    while j < n:
        if s[j] == '1':
            x = j
            while s[j] == '1':
                j += 1
                if j == n:
                    break
            y = j - 1
            l.append([x, y])
        else:
            j += 1
    ans = 0
    j = 0
    while j < len(l):
        if j == 0:
            ans += a
        else:
            ans += min(a, b * (l[j][0] - l[j - 1][1] - 1))
        j += 1
    print(ans)
