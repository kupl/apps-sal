n = int(input())
a = list(map(int, input().split()))
k = float('inf')
for i in range(n):
    if i == 0:
        x = min(a[0], a[-1])
        y = n - 1
        z = x // y
        k = min(k, z)
    elif i == n - 1:
        x = min(a[0], a[-1])
        y = n - 1
        z = x // y
        k = min(k, z)
    else:
        x = min(a[i], a[0])
        y = i
        z = x // y
        k = min(k, z)
        x = min(a[i], a[-1])
        y = n - i - 1
        z = x // y
        k = min(k, z)
print(k)


