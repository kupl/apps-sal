n = int(input())
l = [1] * n
r = [1] * n
a = list(map(int, input().split()))
for i in range(1, n):
    if a[i - 1] < a[i]:
        l[i] += l[i - 1]
for i in range(n - 2, -1, -1):
    if a[i] < a[i + 1]:
        r[i] += r[i + 1]
ans = max(l)
if ans < n:
    ans += 1
for i in range(1, n - 1):
    if a[i - 1] + 1 < a[i + 1]:
        ans = max(ans, l[i - 1] + 1 + r[i + 1])
    else:
        ans = max(ans, l[i - 1] + 1)
print(ans)
