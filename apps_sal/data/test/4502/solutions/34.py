n = int(input())
a = list(map(int, input().split()))
b = []
if n % 2 == 0:
    for i in range(n // 2):
        b.append(a[n - 1 - 2 * i])
    for i in range(n // 2):
        b.append(a[2 * i])
else:
    for i in range((n + 1) // 2):
        b.append(a[n - 1 - 2 * i])
    for i in range((n - 1) // 2):
        b.append(a[1 + 2 * i])
print(*b)
