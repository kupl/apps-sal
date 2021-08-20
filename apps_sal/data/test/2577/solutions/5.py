t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    f = []
    a = []
    for i in range(n):
        g = list(map(int, input().split()))
        if i % 2 == 0:
            for j in range(m):
                if j % 2 == 0:
                    if g[j] % 2 == 0:
                        pass
                    else:
                        g[j] += 1
                elif g[j] % 2 == 1:
                    pass
                else:
                    g[j] += 1
        else:
            for j in range(m):
                if j % 2 == 0:
                    if g[j] % 2 == 1:
                        pass
                    else:
                        g[j] += 1
                elif g[j] % 2 == 0:
                    pass
                else:
                    g[j] += 1
        f.append(g)
    for i in range(n):
        for j in range(m):
            print(f[i][j], end=' ')
        print()
