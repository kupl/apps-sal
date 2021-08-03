for qq in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    last = [-1] * (n + 1)
    dura = [-1] * (n + 1)
    for i in range(n):
        dura[a[i]] = max(dura[a[i]], i - last[a[i]] - 1)
        last[a[i]] = i
    for i in range(n + 1):
        dura[i] = max(dura[i], n - last[i] - 1)

    ans = [n + 1] * n
    for i in range(n + 1):
        if dura[i] == n:
            continue
        ans[dura[i]] = min(ans[dura[i]], i)
    for i in range(n - 1):
        ans[i + 1] = min(ans[i + 1], ans[i])
    for i in range(n):
        if ans[i] == n + 1:
            ans[i] = -1
    print(*ans)
