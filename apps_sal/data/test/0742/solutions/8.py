t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    used = [0 for i in range(2 * n + 1)]
    flg = 1
    for i in range(n):
        if b[i] > i * 2 + 1:
            print(-1)
            flg = 0
            break
        used[b[i]] = 1
    if flg == 0:
        continue
    ans = []
    for i in range(n):
        ans.append(a[i])
        for j in range(a[i], 2 * n + 1):
            if used[j] == 0:
                ans.append(j)
                used[j] = 1
                break
    print(*ans)
