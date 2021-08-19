(n, t, c) = map(int, input().split())
a = list(map(int, input().split()))
b = 0
ans = 0
for i in range(n):
    if a[i] > t:
        ans += max(i - b - c + 1, 0)
        b = i + 1
ans += max(n - b - c + 1, 0)
print(ans)
