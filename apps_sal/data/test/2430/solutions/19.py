n = int(input())
a = []
for i in range(0, n):
    a.append(int(input()))
ans = 0
ans += a[0]
ans += 1
for i in range(0, n - 1):
    if(a[i] <= a[i + 1]):
        ans += 1
        ans += a[i + 1] - a[i]
        ans += 1
    else:
        ans += a[i] - a[i + 1]
        ans += 1
        ans += 1
print(ans)
