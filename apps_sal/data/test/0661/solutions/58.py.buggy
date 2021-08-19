def xor_matching(M, K):
    # 0と1はコーナーケースっぽい
    if M == 0:
        return [0, 0] if K == 0 else [-1]
    if M == 1:
        return [0, 1, 1, 0] if K == 0 else [-1]

    if K >= (1 << M):
        return [-1]

    values = list(range(1 << M))
    Amax = values[-1]
    res = []
    res.append(K)
    for v in values:
        if v == K:
            continue
        res.append(v)
    res.append(K)
    for v in values[::-1]:
        if v == K:
            continue
        res.append(v)
    return res


def __starting_point():
    M, K = list(map(int, input().split()))
    ans = xor_matching(M, K)
    print((*ans))


__starting_point()
