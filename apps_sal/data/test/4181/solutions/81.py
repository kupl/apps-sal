n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.append(0)
ans = min(a[0], b[0])
b[0] = max(0, b[0] - a[0])
for i in range(n):
    ans += min(a[i + 1], b[i])
    a[i + 1] = max(0, a[i + 1] - b[i])
    ans += min(a[i + 1], b[i + 1])
    b[i + 1] = max(0, b[i + 1] - a[i + 1])
print(ans)
