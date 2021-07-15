n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
for i in range(1, n):
    a[i] += a[i - 1]

current = 1
for i in range(n):
    page = a[i] // m + 1
    print(page - current, end = " ")
    current = page
print()
