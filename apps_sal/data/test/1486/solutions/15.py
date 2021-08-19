n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n):
    if i == 0:
        print(a[i + 1] - a[i], a[n - 1] - a[i])
    elif i == n - 1:
        print(a[i] - a[i - 1], a[i] - a[0])
    else:
        print(min(a[i] - a[i - 1], a[i + 1] - a[i]), max(a[i] - a[0], a[n - 1] - a[i]))
