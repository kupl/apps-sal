
from collections import defaultdict

try:
    while True:
        n, m = list(map(int, input().split()))
        f = list(map(int, input().split()))
        b = list(map(int, input().split()))
        d = [[] for i in range(n + 1)]
        for i, x in enumerate(f, 1):
            d[x].append(i)
        a = [None] * m
        ambigious = False
        for i in range(m):
            x = d[b[i]]
            if not x:
                print("Impossible")
                break
            if len(x) != 1:
                ambigious = True
            else:
                a[i] = x[0]
        else:
            if ambigious:
                print("Ambiguity")
            else:
                print("Possible")
                print(' '.join(map(str, a)))
except EOFError:
    pass
