(N, x) = list(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0
if a[0] > x:
    ans += a[0] - x
    a[0] = x
for i in range(N - 1):
    if a[i] + a[i + 1] > x:
        cnt = a[i] + a[i + 1] - x
        ans += cnt
        a[i + 1] -= cnt
print(ans)
