n, m = [int(x) for x in input().split()]
a = sorted([int(x) for x in input().split()])
Min = a[n - 1] - a[0]
for i in range(m - n + 1):
    x = a[i + n - 1] - a[i]
    if x < Min:
        Min = x
print(Min)
