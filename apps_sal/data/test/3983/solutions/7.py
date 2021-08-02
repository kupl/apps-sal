def par(a):
    L = []
    while P[a] >= 0:
        L.append(a)
        a = P[a]
    for l in L:
        P[l] = a
    return a


def unite(a, b):
    if par(a) != par(b):
        if P[par(b)] >= P[par(a)]:
            if P[par(b)] == P[par(a)]:
                P[par(a)] -= 1
            P[par(b)] = par(a)
        else:
            P[par(a)] = par(b)


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    P = [-1] * N
    for _ in range(M):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        unite(a, b)
    p1, p2 = par(0), par(N - 1)
    c1, c2 = 0, 0
    for i in range(N):
        pi = par(i)
        if pi == p1:
            c1 ^= 1
        elif pi == p2:
            c2 ^= 1

    if N % 4 == 1:
        if M % 2:
            print("First")
        else:
            print("Second")
    elif N % 4 == 3:
        if M % 2 == 0:
            print("First")
        else:
            print("Second")
    elif c1 ^ c2:
        print("First")
    elif N % 4 == 0:
        if c1 ^ (M & 1) == 0:
            print("Second")
        else:
            print("First")
    elif N % 4 == 2:
        if c1 ^ (M & 1):
            print("Second")
        else:
            print("First")
