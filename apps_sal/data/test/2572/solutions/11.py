t = int(input())
for u in range(t):
    x = [int(x) for x in input().split()]
    n = x[0]
    m = x[1]
    k = [[[] for j in range((m + 1) // 2)] for i in range((n + 1) // 2)]
    for i in range(n // 2):
        inp = [int(x) for x in input().split()]
        for j in range(m // 2):
            k[i][j].append(inp[j])
        for j in range((m + 1) // 2):
            k[i][j].append(inp[m - j - 1])
    for i in range((n + 1) // 2):
        inp = [int(x) for x in input().split()]
        for j in range(m // 2):
            k[(n + 1) // 2 - 1 - i][j].append(inp[j])
        for j in range((m + 1) // 2):
            k[(n + 1) // 2 - 1 - i][j].append(inp[m - j - 1])
    ans = 0
    for i in range((n + 1) // 2):
        for j in range((m + 1) // 2):
            if i == n // 2:
                if j != m // 2:
                    ans += max(k[i][j]) - min(k[i][j])
            elif j == m // 2:
                ans += max(k[i][j]) - min(k[i][j])
            else:
                k[i][j].sort()
                ans += k[i][j][3]
                ans += k[i][j][2]
                ans -= k[i][j][1]
                ans -= k[i][j][0]
    print(ans)
