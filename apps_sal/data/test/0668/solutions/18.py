def dfs(v):
    was[v] = 1
    cnt = 0
    for i in range(v + 1, n):
        if cnt >= a[v][0]:
            break
        if not was[i]:
            cnt += 1
            ans.append((a[v][1], a[i][1]))
            dfs(i)

n = int(input())
a = list(map(int, input().split()))
a = [(a[i], i + 1) for i in range(n)]
a = [a[0]] + sorted(a[1:])[::-1]
ans = []
was = [0] * n
dfs(0)
if was.count(0):
    print(-1)
else:
    print(len(ans))
    [print(*i) for i in ans]
