import itertools


def main():
    (N, M, Q) = list(map(int, input().split()))
    a = []
    b = []
    c = []
    d = []
    for i in range(Q):
        (ai, bi, ci, di) = list(map(int, input().split()))
        a.append(ai)
        b.append(bi)
        c.append(ci)
        d.append(di)
    ans = 0
    for A in list(itertools.combinations_with_replacement(list(range(1, M + 1)), N)):
        score = 0
        for i in range(Q):
            if A[b[i] - 1] - A[a[i] - 1] == c[i]:
                score += d[i]
        if ans < score:
            ans = score
    print(ans)


def __starting_point():
    main()


__starting_point()
