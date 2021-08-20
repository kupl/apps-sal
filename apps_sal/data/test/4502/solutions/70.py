n = int(input())
a = [int(x) for x in input().split()]
b = []
if n % 2 == 0:
    i = n - 1
    while i >= 0:
        b.append(a[i])
        i -= 2
    i = 0
    while i < n:
        b.append(a[i])
        i += 2
else:
    i = n - 1
    while i >= 0:
        b.append(a[i])
        i -= 2
    i = 1
    while i < n:
        b.append(a[i])
        i += 2
b = [str(x) for x in b]
print(' '.join(b))
