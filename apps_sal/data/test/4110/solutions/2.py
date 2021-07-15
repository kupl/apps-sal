def dfs(i, sum, count, rest):
    nonlocal ans
    if i == d:
        if sum < g:
            rest_max = max(rest)
            n = min(l[rest_max-1][0], -(-(g-sum)//(rest_max*100)))
            count += n
            sum += n * rest_max * 100
        if sum >= g:
            ans = min(ans, count)
    else :
        dfs(i+1, sum, count, rest) #二分岐のうち解かない選択
        dfs(i+1, sum + l[i][0]*(i+1)*100+l[i][1], count + l[i][0], rest - {i+1}) #解く選択

d, g = list(map(int, input().split()))
l = [list((list(map(int, input().split())))) for _ in range(d)]
ans = float("inf")
dfs(0, 0, 0, set(range(1, d+1)))
print(ans)

