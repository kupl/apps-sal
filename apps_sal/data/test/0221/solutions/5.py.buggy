n, k = map(int, input().strip().split())
f = 2 * k + 1
g = n // f
h = n % f
if (h == 0):
    print(g)
    c1 = k + 1
    print(c1, end=" ")
    for i in range(1, g):
        print(c1 + f * i, end=" ")
    print()
    return
if (h > k):
    print(g + 1)
    e = h - k
    print(e, end=" ")
    for i in range(1, g + 1):
        print(e + f * i, end=" ")
    print()
    return
if (h <= k):
    print(g + 1)
    t = h + 2 * k + 1
    e = 1
    print(1, end=" ")
    for i in range(1, g + 1):
        print(e + f * i, end=" ")
    print()
    return
