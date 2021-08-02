n = int(input())
a = list(map(int, input().split()))
x = sum(a)
b = list(map(int, input().split()))
for i in range(n):
    if (a[i] < b[i]):
        tmp = b[i] - a[i]
        a[i + 1] = a[i + 1] - tmp
        a[i] = 0
        if (a[i + 1] < 0):
            a[i + 1] = 0
    else:
        a[i] = a[i] - b[i]

print((x - sum(a)))
