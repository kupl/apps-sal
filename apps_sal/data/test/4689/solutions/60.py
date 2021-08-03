l, n = map(int, input().split())
a = input().split()
for i in range(n):
    a[i] = (int)(a[i])

min = l + a[0] - a[n - 1]
for i in range(n - 1):
    if min < a[i + 1] - a[i]:
        min = a[i + 1] - a[i]
print(l - min)
