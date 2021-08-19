from sys import stdin
(n, m) = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
x = 1 << n
arr = [0] * (2 * x)
for j in range(x, 2 * x):
    arr[j] = lst[j - x]
y = x
while y != 1:
    for j in range(y, 2 * y, 2):
        arr[j // 2] = arr[j] | arr[j + 1]
    y >>= 1
    if y == 1:
        break
    for j in range(y, 2 * y, 2):
        arr[j // 2] = arr[j] ^ arr[j + 1]
    y >>= 1
for _ in range(m):
    (p, b) = map(int, stdin.readline().split())
    z = x + p - 1
    arr[z] = b
    while z != 1:
        if z % 2 == 0:
            v = z + 1
        else:
            v = z - 1
        ch = arr[z] | arr[v]
        z >>= 1
        arr[z] = ch
        if z == 1:
            break
        if z % 2 == 0:
            v = z + 1
        else:
            v = z - 1
        ch = arr[z] ^ arr[v]
        z >>= 1
        arr[z] = ch
    print(arr[1])
