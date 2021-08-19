t = int(input())
for you in range(t):
    l = input().split()
    n = int(l[0])
    m = int(l[1])
    l = []
    for i in range(n):
        lo = input().split()
        li = [int(i) for i in lo]
        l.append(li)
    ans = 0
    for i in range((n + 1) // 2):
        for j in range((m + 1) // 2):
            lp = []
            num1 = l[i][j]
            lp.append(num1)
            num2 = l[n - i - 1][j]
            if n - 1 - i != i:
                lp.append(num2)
            num3 = l[i][m - 1 - j]
            if m - 1 - j != j:
                lp.append(num3)
            num4 = l[n - 1 - i][m - 1 - j]
            if n - 1 - i != i and m - 1 - j != j:
                lp.append(num4)
            lp.sort()
            z = len(lp)
            for k in range(z):
                ans = ans + abs(lp[k] - lp[z // 2])
    print(ans)
