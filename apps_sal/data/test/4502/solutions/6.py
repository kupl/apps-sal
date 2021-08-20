n = int(input())
a = list(map(int, input().split()))
b = [0] * n
if n % 2 == 0:
    c = n // 2 - 1
else:
    c = n // 2
b[c] = a[0]
for i in range(1, n):
    if i % 2 == 1:
        b[c + i] = a[i]
        c += i
    else:
        b[c - i] = a[i]
        c -= i
if c != 0:
    b.reverse()
    print(*b, sep=' ')
else:
    print(*b, sep=' ')
