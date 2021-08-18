n, k = list(map(int, input().split()))
v = list(map(int, input().split()))

ans = 0
for l in range(0, k + 1):
    for r in range(0, k + 1 - l):
        if l + r > n:
            continue
        suteru = k - l - r
        get = []
        for i in range(l):
            get.append(v[i])
        for i in range(n - 1, n - 1 - r, -1):
            get.append(v[i])
        get.sort()
        minus = 0
        while minus < min(suteru, len(get)) and get[minus] < 0:
            minus += 1
        ans = max(ans, sum(get[minus:]))
print(ans)
