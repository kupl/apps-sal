(n, d) = list(map(int, input().split()))
c = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        ans = 0
        for k in range(d):
            ans += abs(c[i][k] - c[j][k]) ** 2
        ans = ans ** 0.5
        if ans.is_integer():
            cnt += 1
print(cnt)
