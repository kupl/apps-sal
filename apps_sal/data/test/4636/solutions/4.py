for _ in range(int(input())):
    n = int(input())
    L = list(map(int, input().split()))
    (a, b) = (0, 0)
    (la, lb) = (0, 0)
    (i, j) = (0, n - 1)
    rnds = 0
    while i <= j:
        ca = 0
        while i <= j and ca <= lb:
            ca += L[i]
            i += 1
        a += ca
        la = ca
        rnds += 1
        if i > j:
            break
        cb = 0
        while i <= j and cb <= la:
            cb += L[j]
            j -= 1
        b += cb
        lb = cb
        rnds += 1
    print(rnds, a, b)
