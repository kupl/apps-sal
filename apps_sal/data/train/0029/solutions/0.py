input = __import__('sys').stdin.readline
for _ in range(int(input())):
    n = int(input())
    s = list(map(int, input().split()))
    g = [[-1]for _ in range(n + 1)]
    for i in range(n):
        g[s[i]].append(i)
    inf = 10**10
    ans = [-1] * n
    lstunused = n
    for i in range(1, n + 1):
        g[i].append(n)
        mx = 0
        for j in range(1, len(g[i])):
            mx = max(mx, g[i][j] - g[i][j - 1] - 1)
        for j in range(mx, lstunused):
            ans[j] = i
        lstunused = min(lstunused, mx)
    print(*ans)
