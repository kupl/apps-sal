(n, k) = map(int, input().split())
a = []
s0 = []
s1 = []
s2 = []
ans = 0
for i in range(n):
    s = list(input())
    a.append(s)
    for j in range(12):
        if s[j] == '.':
            if j == 0:
                if s[j + 1] == 'S':
                    s1.append((i, j))
                else:
                    s0.append((i, j))
            elif j == 11:
                if s[j - 1] == 'S':
                    s1.append((i, j))
                else:
                    s0.append((i, j))
            elif s[j - 1] == 'S' and s[j + 1] == 'S':
                s2.append((i, j))
            elif s[j - 1] != 'S' and s[j + 1] != 'S':
                s0.append((i, j))
            else:
                s1.append((i, j))
        if s[j] == 'S':
            if j > 0 and (s[j - 1] == 'P' or s[j - 1] == 'S'):
                ans += 1
            if j < 11 and (s[j + 1] == 'P' or s[j + 1] == 'S'):
                ans += 1
p0 = 0
p1 = 0
p2 = 0
for g in range(k):
    if p0 < len(s0):
        (i, j) = s0[p0]
        p0 += 1
        a[i][j] = 'x'
    elif p1 < len(s1):
        (i, j) = s1[p1]
        p1 += 1
        a[i][j] = 'x'
        ans += 1
    else:
        (i, j) = s2[p2]
        p2 += 1
        a[i][j] = 'x'
        ans += 2
print(ans)
for s in a:
    print(''.join(s))
