def dfs(lst):
    nonlocal ans
    if len(lst) > n:
        return
    lowest = 1
    if lst != []:
        lowest = lst[-1]
    for i in range(lowest, m + 1):
        lst.append(i)
        dfs(lst)
        lst.pop()
    if len(lst) == n:
        cnt = 0
        for i in range(q):
            a, b, c, d = ab[i]
            if lst[b - 1] - lst[a - 1] == c:
                cnt += d
        ans = max(cnt, ans)


n, m, q = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(q)]
ans = 0
dfs([])

print(ans)
