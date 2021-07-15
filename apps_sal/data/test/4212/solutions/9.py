def dfs(s):
    nonlocal ans
    if len(s) == n:
        cnt = 0
        for i in range(q):
            if s[abcd[i][1]-1]-s[abcd[i][0]-1] == abcd[i][2]:
                cnt += abcd[i][3]
        ans = max(ans, cnt)
        return
    last = 1
    if len(s) > 0:
        last = s[-1]
    for i in range(last, m+1):
        dfs(s+[i])
    return

n, m, q = map(int, input().split())
abcd = [list(map(int, input().split())) for i in range(q)]
ans = 0
dfs([])
print(ans)
