n = int(input())
a = list(map(int, input().split()))

s = sum(a)
x = 0
ans = abs(2 * a[0] - s)
snuke = a[0]

for i in range(1, n - 1):
    snuke += a[i]
    if abs(2 * snuke - s) < ans:
        ans = abs(2 * snuke - s)

print(ans)
