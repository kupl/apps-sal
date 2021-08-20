mod = 10 ** 9 + 7
n = int(input())
a = [0] * n
x = n - 1
for i in range(n - 1, -1, -1):
    if i == n - 1:
        a[i] = n
    elif i == n - 2:
        a[i] = n * n
    else:
        x -= 1
        x += a[i + 3] if i + 3 < n else 1
        x %= mod
        a[i] += a[i + 1] + (n - 1) * (n - 1) + x
    a[i] %= mod
print(a[0])
