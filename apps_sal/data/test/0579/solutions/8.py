from itertools import accumulate


def main():
    (n, k) = list(map(int, input().split()))
    P = [int(x) - 1 for x in input().split()]
    C = [int(x) for x in input().split()]
    F = [False] * n
    a = -10 ** 9
    for i in range(n):
        if F[i]:
            continue
        (p, F[i], L) = (i, True, [C[i]])
        while P[p] != i:
            p = P[p]
            F[p] = True
            L.append(C[p])
        (t, l) = (sum(L), len(L))
        s = t * (k // l - 1) if t > 0 else 0
        (m, L) = (-10 ** 9, L * 3)
        u = k % l + l if t > 0 else min(k, l)
        for j in range(l):
            m = max(m, max(accumulate(L[j:j + u])))
        a = max(s + m, a)
    print(a)


main()
