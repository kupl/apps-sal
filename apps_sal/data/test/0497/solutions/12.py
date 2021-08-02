n = int(input())
a = list(map(int, input().split()))
max1 = max2 = 0
for q in range(1, n):
    if a[0] != a[q]:
        max1 = q
for q in range(n - 2, -1, -1):
    if a[-1] != a[q]:
        max2 = q
print(max(max1, n - max2 - 1))
