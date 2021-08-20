(n, m) = list(map(int, input().split()))
mp = []
for i in range(n):
    line = input().strip()
    mp.append(list([c == '#' for c in line]))
mp1 = [[False for _ in range(m)] for _ in range(n)]
for i in range(1, n - 1):
    for j in range(1, m - 1):
        f = all((mp[i - 1][j - k] for k in range(-1, 1 + 1)))
        f = f and all((mp[i + 1][j - k] for k in range(-1, 1 + 1)))
        f = f and (mp[i][j - 1] and mp[i][j + 1])
        if not f:
            continue
        for ik in range(-1, 2):
            for jk in range(-1, 2):
                if ik == 0 and jk == 0:
                    continue
                mp1[i + ik][j + jk] = True
if all((all((mp[i][j] == mp1[i][j] for j in range(m))) for i in range(n))):
    print('YES')
else:
    print('NO')
