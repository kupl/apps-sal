n = int(input())
a = [int(input()) for i in range(n)]
b = [0] * n
c = 1
for i in range(n):
    b[i] = a[i] // 2
    if a[i] % 2:
        b[i] += c
        c ^= 1
print('\n'.join(map(str, b)))
