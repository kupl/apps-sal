n = int(input())
a = list(map(int, input().split()))
ans = n * n * (n + 1) // 2
rd = 0
for i in range(n - 1):
    l = min(a[i], a[i + 1])
    r = max(a[i], a[i + 1])
    rd += l * (n - r + 1)
for i in range(n):
    rd += max((a[i] - 2) * (a[i] - 1) // 2, 0)
    rd += n - 1
    rd += (n - a[i]) * (n - a[i] - 1) // 2
ans -= rd
print(ans)
