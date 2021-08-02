n = int(input())
a = list(map(int, input().split()))

ans = 0
for i in range(1, n - 1):
    if a[i] > max(a[i - 1], a[i + 1]) or a[i] < min(a[i - 1], a[i + 1]):
        ans += 1

print(ans)
