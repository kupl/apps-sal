def main():
    n = int(input())
    P = [int(x) - 1 for x in input().split()]
    Q = [0] * n

    for i, p in enumerate(P):
        Q[p] = i

    L, i = [], n - 1
    while i > 0:
        if i == Q[i]:
            print((-1))
            return
        for j in range(Q[i], i):
            P[j], P[j + 1] = P[j + 1], P[j]
            L.append(j + 1)
        for j in range(Q[i] + 1, i + 1):
            if P[j] != j:
                print((-1))
                return
        i = Q[i]

    for l in L:
        print(l)


main()
