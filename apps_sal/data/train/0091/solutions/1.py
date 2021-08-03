t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [0] * n
    m = 0
    c = set(range(1, n + 1))
    for i in range(n):
        if a[i] > m:
            b[i] = a[i]
            m = a[i]
            c.discard(a[i])
    c = sorted(c)
    j = 0
    for i in range(n):
        if b[i] == 0:
            b[i] = c[j]
            j += 1
            if b[i] > a[i]:
                print(-1)
                break
    else:
        print(*b)
