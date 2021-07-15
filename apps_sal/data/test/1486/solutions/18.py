n = int(input())
a = list(map(int, input().split()))
mini = 0
maxi = 0
for i in range(n):
    if i != 0 and i != n - 1:
        mini = abs(a[i - 1] - a[i])
        mini = min(mini, abs(a[i + 1] - a[i]))
        maxi = max(abs(a[0] - a[i]), abs(a[-1] - a[i]))
        print(mini, maxi)
    elif i == 0:
        print(abs(a[i + 1] - a[i]), abs(a[i] - a[-1]))
    else:
        print(abs(a[i - 1] - a[i]), abs(a[i] - a[0]))

