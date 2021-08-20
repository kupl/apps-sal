n = int(input())
a = list(map(int, input().split()))
for i in range(n - 1):
    if (i + 1) % 2 == 1:
        if a[i] > a[i + 1]:
            t = a[i]
            a[i] = a[i + 1]
            a[i + 1] = t
        else:
            pass
    elif a[i] < a[i + 1]:
        t = a[i]
        a[i] = a[i + 1]
        a[i + 1] = t
    else:
        pass
for i in range(n):
    print(a[i], end=' ')
