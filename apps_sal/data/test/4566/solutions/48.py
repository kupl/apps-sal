n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
ans = []
for i in range(n):
    cnt = 0
    for j in range(m):
        if ab[j][0] == i + 1 or ab[j][1] == i + 1:
            cnt += 1
    ans.append(cnt)
for k in range(n):
    print(ans[k])
