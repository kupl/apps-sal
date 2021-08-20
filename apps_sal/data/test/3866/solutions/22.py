n = int(input())
(a, b) = ([], [])
c = []
if n % 2 != 0:
    for i in range(n):
        a += [i]
        b += [i]
        c.append((a[i] + b[i]) % n)
    print(*a)
    print(*b)
    print(*c)
else:
    print(-1)
