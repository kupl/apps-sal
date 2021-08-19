(n, m) = list(map(int, input().split()))
h = list(map(int, input().split()))
ab = [list(map(int, input().split())) for _ in range(m)]
ans = [1] * n
for i in range(m):
    if h[ab[i][0] - 1] == h[ab[i][1] - 1]:
        ans[ab[i][0] - 1] = 0
        ans[ab[i][1] - 1] = 0
    elif h[ab[i][0] - 1] > h[ab[i][1] - 1]:
        ans[ab[i][1] - 1] = 0
    else:
        ans[ab[i][0] - 1] = 0
print(sum(ans))
