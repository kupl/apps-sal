n = int(input())
a = list(map(int, input().split()))
b = [-1] * n
b[0] = 0; b[n - 1] = a[0]
for i in range(1, n // 2):
    p, q = 0, a[i]
    fl = 1
    if p >= b[i - 1] and q <= b[n - i] and fl:
        b[i] = p
        b[n - i - 1] = q
        fl = 0
    p = b[i - 1]; q = a[i] - b[i - 1]
    if p >= b[i - 1] and q <= b[n - i] and fl:
        b[i] = p
        b[n - i - 1] = q
        fl = 0
    q = b[n - i]; p = a[i] - b[n - i]
    if p >= b[i - 1] and q <= b[n - i] and fl:
        b[i] = p
        b[n - i - 1] = q
        fl = 0
print(*b)
