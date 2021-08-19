def solve(n):
    a = []
    b = []
    c = []
    for i in range(n):
        a.append(i)
    for i in range(1, n):
        b.append(i)
    b.append(0)
    for i in range(n):
        if a[i] + b[i] < n:
            c.append(a[i] + b[i])
        elif a[i] + b[i] == n:
            c.append(0)
        else:
            c.append(a[i] + b[i] - n)
    if len(c) != len(set(c)):
        print(-1)
    else:
        print(' '.join(map(str, a)))
        print(' '.join(map(str, b)))
        print(' '.join(map(str, c)))


def __starting_point():
    n = int(input())
    solve(n)


__starting_point()
