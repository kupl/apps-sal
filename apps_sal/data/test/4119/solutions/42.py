n, m = map(int, input().split())
li_X = list(map(int, input().split()))

li_X.sort()
li_X_delta = []
for i in range(len(li_X) - 1):
    li_X_delta.append(li_X[i + 1] - li_X[i])
li_X_delta.sort(reverse=True)
cnt = 0

ans = li_X[-1] - li_X[0]
for i in range(min(n - 1, len(li_X_delta))):
    ans -= li_X_delta[i]
print(ans)
