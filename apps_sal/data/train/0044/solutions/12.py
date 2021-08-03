for i in range(int(input())):
    n = int(input())
    g = []
    c = 4 * n
    for j in range(n):
        g.append(c)
        c = c - 2
    print(' '.join(map(str, g)))
