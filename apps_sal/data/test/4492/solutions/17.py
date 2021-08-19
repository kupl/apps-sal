(N, x) = map(int, input().split())
ls = list(map(int, input().split()))
ans = 0
for i in range(N - 1):
    if ls[i] + ls[i + 1] <= x:
        continue
    else:
        eat = -x + ls[i] + ls[i + 1]
        ls[i + 1] -= eat
        if ls[i + 1] < 0:
            ls[i + 1] = 0
        ans += eat
print(ans)
