def rec(l, n):
    c = 0
    for i in (1, 2, 3, 4, 5, 6, 7, 8, 9):
        if (int(str(i) * l) <= n):
            c += 1
        else:
            return (c, 0)
    return (c, 1)

t = int(input())
for i in range(t):
    n = int(input())
    c = 0
    x = 1
    ans = (0, 1)
    while (ans[1]):
        ans = rec(x, n)
        c += ans[0]
        x += 1
    print(c)

