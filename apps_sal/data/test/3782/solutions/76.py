def search(x, K, Q, A):
    cand = []
    i = 0
    while i < len(A):
        tmp = []
        while i < len(A):
            if A[i] >= x:
                tmp.append(A[i])
                i += 1
            else:
                i += 1
                break
        if len(tmp) >= K:
            tmp.sort()
            L = len(tmp) - K + 1
            cand.extend(tmp[:L])
    if len(cand) < Q:
        return -1
    else:
        return sorted(cand)[Q - 1]


def main():
    (N, K, Q) = map(int, input().split())
    A = list(map(int, input().split()))
    if Q == 1:
        return 0
    res = 10 ** 18
    for (i, x) in enumerate(A):
        rest = A[:i] + A[i + 1:]
        y = search(x, K, Q - 1, rest)
        if y == -1:
            continue
        res = min(res, y - x)
    return res


def __starting_point():
    print(main())


__starting_point()
