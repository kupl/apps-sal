n = int(input())
a = list(map(int, input().split()))
b = []
if n % 2 == 0:
    for i in range(n - 1, 0, -2):
        b.append(a[i])
    for i in range(0, n - 1, 2):
        b.append(a[i])
else:
    for i in range(n - 1, -1, -2):
        b.append(a[i])
    for i in range(1, n - 1, 2):
        b.append(a[i])
print(*b)
