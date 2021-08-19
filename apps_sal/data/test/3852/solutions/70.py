n = int(input())
a = list(map(int, input().split()))
ans = []
mx = 0
for i in range(n):
    if abs(a[i]) > abs(mx):
        mx = a[i]
        mx_idx = i
for i in range(n):
    if mx * a[i] < 0:
        ans.append((mx_idx + 1, i + 1))
for i in range(n - 1):
    if mx > 0:
        ans.append((i + 1, i + 2))
    elif mx < 0:
        ans.append((n - i, n - i - 1))
print(len(ans))
for (x, y) in ans:
    print(x, y)
