def main():
    import sys
    from collections import deque
    x0, y0, x1, y1 = map(int, input().strip().split())
    n = int(input())
    S = list(map(int, sys.stdin.read().strip().split()))
    h = set()
    d = {}

    def getchild(a):
        c = []
        xc = [1, -1, 0, 0, 1, 1, -1, -1]
        yc = [0, 0, 1, -1, 1, -1, 1, -1]
        for i in range(8):
            if ((a[0] + xc[i], a[1] + yc[i]) in h):
                c.append((a[0] + xc[i], a[1] + yc[i]))
        return(c)

    class g:
        def __init__(self):
            self.depth = -1
            self.child = []

    for i in range(0, 3 * n, 3):
        r, a, b = S[i], S[i + 1], S[i + 2]
        for j in range(a, b + 1):
            h.add((r, j))
            d[(r, j)] = g()
    king = d[(x0, y0)]
    destination = d[(x1, y1)]
    for i in h:
        d[i].child = getchild(i)

    Q = deque()
    Q.append(king)
    king.depth = 0
    while(len(Q) > 0):
        a = Q.popleft()
        for i in a.child:
            if d[i].depth == -1:
                Q.append(d[i])
                d[i].depth = a.depth + 1
        if a == destination:
            break
    print(destination.depth)


main()
