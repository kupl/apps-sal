n = int(input())
a = list(map(int, input().split()))
sum1 = 0
for x in range(n - 1):
    sum1 += abs(a[x] - a[x + 1])
sum1 += abs(a[0]) + abs(a[n - 1])
for y in range(n):
    if y == 0:
        print(sum1 - abs(a[0]) - abs(a[1] - a[0]) + abs(a[1]))
    elif y == n - 1:
        print(sum1 - abs(a[n - 1] - a[n - 2]) - abs(a[n - 1]) + abs(a[n - 2]))
    else:
        print(sum1 - abs(a[y] - a[y - 1]) - abs(a[y] - a[y + 1]) + abs(a[y - 1] - a[y + 1]))
