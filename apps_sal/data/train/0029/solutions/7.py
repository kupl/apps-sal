INF = 10 ** 15


for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    d = {i: 0 for i in arr}
    last = {i: -1 for i in arr}
    for i in range(n):
        if last[arr[i]] == -1:
            d[arr[i]] = max(d[arr[i]], i + 1)
        else:
            d[arr[i]] = max(d[arr[i]], i - last[arr[i]])
        last[arr[i]] = i

    for i in list(last.keys()):
        d[i] = max(d[i], n - last[i])

    d2 = {}
    for k, v in list(d.items()):
        if v not in d2:
            d2[v] = INF
        d2[v] = min(d2[v], k)

    ans = [INF] * n
    for i in range(1, n + 1):
        can = INF
        if i != 1:
            can = ans[i - 2]
        if i in list(d2.keys()):
            can = min(can, d2[i])
        ans[i - 1] = can

    for i in range(n):
        if ans[i] == INF:
            ans[i] = -1

    print(*ans)
