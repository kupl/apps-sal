T = int(input())

for t in range(T):
    N = int(input())

    P = [int(_) for _ in input().split()]
    up = P[1] > P[0]
    res = [P[0]]

    for i in range(1, N-1):
        if up and P[i+1] < P[i]:
            res.append(P[i])
            up = False
        elif not up and P[i+1] > P[i]:
            res.append(P[i])
            up = True

    if P[N-1] != P[N-2]:
        res.append(P[N-1])

    print(len(res))
    print(' '.join(map(str, res)))

