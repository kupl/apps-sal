def dfs(i, sum, count, nokori):
    nonlocal ans
    if i == d:
        if sum < g:
            use = max(nokori)

            n = min(pc[use - 1][0], -(-(g - sum) // (use * 100)))
            count += n
            sum += n * use * 100

        if sum >= g:
            ans = min(ans, count)
            
    else:
        dfs(i+1, sum, count, nokori)
        dfs(i+1, sum + pc[i][0] * (i+1) * 100 + pc[i][1], count + pc[i][0], nokori - {i + 1})


d, g = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(d)]

ans = float("inf")

dfs(0, 0, 0, set(range(1, d+1)))
print(ans)
