n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = 10**10
for i in range(n - k + 1):
    tmp = min(abs(a[k + i - 1] - a[i]) + abs(a[i]), abs(a[k + i - 1] - a[i]) + abs(a[k + i - 1]))
    if ans > tmp:
        ans = tmp
print(ans)
