def solve():
    n = int(input())
    s = input()
    l = []
    (g_seg, s_seg) = (0, 0)
    g_count = 0
    for i in range(n):
        if s[i] == 'S':
            if g_seg:
                g_count += 1
                l.append(('G', g_seg))
                g_seg = 0
            s_seg += 1
        else:
            if s_seg:
                l.append(('S', s_seg))
                s_seg = 0
            g_seg += 1
    if g_seg:
        l.append(('G', g_seg))
        g_count += 1
    if not g_count:
        return 0
    if len(l) == 1:
        return l[0][1]
    elif len(l) == 2:
        return l[1][1]
    if g_count == 2:
        ans = 0
        for i in range(len(l) - 2):
            if l[i][0] == 'G':
                if l[i + 1][1] == 1:
                    ans = max(ans, l[i][1] + l[i + 2][1])
                else:
                    ans = max(ans, l[i][1] + 1, l[i + 2][1] + 1)
        return ans
    else:
        ans = 0
        for i in range(len(l) - 2):
            if l[i][0] == 'G':
                if l[i + 1][1] == 1:
                    ans = max(ans, l[i][1] + 1 + l[i + 2][1])
                else:
                    ans = max(ans, l[i][1] + 1, l[i + 2][1] + 1)
        return ans


print(solve())
