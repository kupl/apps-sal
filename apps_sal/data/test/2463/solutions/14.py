n = int(input())
a = list(map(int, input().split()))
a.sort()
print((n - 1) // 2)
for i in range(1, n, 2):
    a[i], a[i - 1] = a[i - 1], a[i]
print(*a)

