(n, m) = list(map(int, input().split()))
t = list(map(int, input().split()))
ans = 0
for i in range(n):
    if i == n - 1:
        ans += m
    elif t[i + 1] - t[i] > m:
        ans += m
    else:
        ans += t[i + 1] - t[i]
print(ans)
