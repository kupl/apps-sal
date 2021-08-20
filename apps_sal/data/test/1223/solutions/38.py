def main():
    N = int(input())
    (*p,) = list(map(int, input().split()))
    xtoi = [-1] * (N + 1)
    for (i, x) in enumerate(p):
        xtoi[x] = i
    L = [-1] * (N + 2)
    R = [N] * (N + 2)
    for i in range(N):
        L[i] = i - 1
        R[i] = i + 1
    iter_inds = iter(xtoi)
    next(iter_inds)
    ans = 0
    for (x, ind) in enumerate(iter_inds, start=1):
        l1 = L[ind]
        l2 = L[l1]
        r1 = R[ind]
        r2 = R[r1]
        ans += x * ((l1 - l2) * (r1 - ind) + (r2 - r1) * (ind - l1))
        L[r1] = l1
        R[l1] = r1
    print(ans)


def __starting_point():
    main()


__starting_point()
