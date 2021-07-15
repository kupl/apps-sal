n = int(input())
a = input()
b = input()
mod = int(1e9+7)
x, y, z = 1, 1, 1
for i in range(n):
    if a[i] == '?' and b[i] == '?':
        x = (x * 55) % mod
        y = (y * 55) % mod
        z = (z * 10) % mod
    elif a[i] == '?':
        x = (x * (10 - int(b[i]))) % mod
        y = (y * (int(b[i]) + 1)) % mod
    elif b[i] == '?':
        x = (x * (int(a[i]) + 1)) % mod
        y = (y * (10 - int(a[i]))) % mod
    else:
        if int(a[i]) < int(b[i]): x = 0
        if int(a[i]) > int(b[i]): y = 0
        if a[i] != b[i]: z = 0
res = pow(10, a.count('?') + b.count('?'), mod)
print((res - x - y + z) % mod)

