for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    c = []
    d = max(a)
    for i in range(n):
        c.append(d - a[i])
    d = max(c)
    e = []
    for i in range(n):
        e.append(d - c[i])
    if k == 0:
        print(*a)
    elif k % 2 == 0:
        print(*e)
    else:
        print(*c)
