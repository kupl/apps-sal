N, M = map(int, input().split())
x = sorted(list(map(int, input().split())))
ans = []
for i in range(M - 1):
    ans.append(x[i + 1] - x[i])
ans = sorted(ans, reverse=True)

print(sum(ans) - sum(ans[0:N - 1]))
