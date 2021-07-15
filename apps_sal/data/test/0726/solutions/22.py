n, d = map(int, input().split())
a = list(map(int, input().split()))
ans = 2
for i in range(n - 1):
    if a[i + 1] - a[i] > 2 * d:
        ans += 2
    elif a[i + 1] - a[i] == 2 * d:
        ans += 1
print(ans)
