def go():
    n, m = list(map(int, input().split()))
    dx = []
    dy = []
    for i in range (0, m):
        a, b = list(map(int, input().split()))
        dx.append(a - 1)
        dy.append(b - 1)
    c = []
    for i in range (0, n):
        c.append(0);
    for i in range (0, m):
        c[ dx[i] ] = c[ dx[i] ] + 1
        c[ dy[i] ] = c[ dy[i] ] + 1
    p = 0
    for i in range (0, n):
        if c[i] == 0:
            p = i
            break
    print(n - 1)
    for i in range (0, n):
        if i != p:
            print(p + 1, i + 1)
def __starting_point():
    go()

__starting_point()
