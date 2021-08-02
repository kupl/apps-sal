def dfs(cnt, lowest, lst):
    nonlocal ans
    if cnt > n:
        return
    for i in range(lowest, m + 1):
        lst.append(i)
        dfs(cnt + 1, i, lst)
        lst.pop()
    if cnt == n:
        num = 0
        for i in range(q):
            a, b, c, d = ab[i]
            if lst[b - 1] - lst[a - 1] == c:
                num += d
        ans = max(num, ans)


n, m, q = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(q)]
ans = 0
dfs(0, 1, [])

print(ans)
