n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
c = 0
for i in range(n - 1):
    if a[i] >= a[i + 1]:
        x = a[i + 1]
        a[i + 1] += a[i] - a[i + 1] + 1
        c += a[i] - x + 1
print(c)
