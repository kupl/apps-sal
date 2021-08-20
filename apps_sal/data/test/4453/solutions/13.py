Q = int(input())
for q in range(Q):
    N = int(input())
    P = list(map(int, input().split()))
    out = []
    i = 1
    for p in P:
        o = 1
        while p != i:
            p = P[p - 1]
            o += 1
        out.append(str(o))
        i += 1
    print(' '.join(out))
