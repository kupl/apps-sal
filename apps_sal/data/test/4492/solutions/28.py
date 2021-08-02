N, x = [int(x) for x in input().split()]
a = list([int(x) for x in input().split()])

count = 0
for i in range(N):
    if a[i] > x:
        count += a[i] - x
        a[i] -= a[i] - x

    if i - 1 >= 0:
        if a[i] + a[i - 1] > x:
            count += (a[i] + a[i - 1]) - x
            a[i] -= (a[i] + a[i - 1]) - x

print(count)
