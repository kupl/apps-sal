n = int(input())
a = [int(i) for i in input().split()]
c = 0
i = 0
while i < n - 1:
    x = a[i]
    y = a[i + 1]
    while y > 0:
        x, y = y, x % y
    if x > 1:
        a = a[:i + 1] + [1] + a[i + 1:]
        i += 2
        c += 1
        n += 1
    else:
        i += 1
print(c)
print(*a)
