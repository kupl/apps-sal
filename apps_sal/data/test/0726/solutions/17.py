n, d = list(map(int, input().split()))
a = list(map(int, input().split()))
a.sort()
a = [-10**10] + a + [10**10]
ans = 0
for i in range(1, n + 1):
    if(abs((a[i] - d) - a[i - 1]) >= d):
        if abs((a[i] - d) - a[i - 1]) != d:
            ans += 1
    if (abs((a[i] + d) - a[i + 1]) >= d):
        ans += 1
print(ans)
