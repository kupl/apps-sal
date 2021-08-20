def main():
    (N, P) = list(map(int, input().split()))
    A = list(map(int, input()))
    if 10 % P == 0:
        ret = 0
        for (i, x) in enumerate(reversed(tuple(A)), start=0):
            if x % P == 0:
                ret += N - i
        print(ret)
        return
    ctr = [0] * P
    ctr[0] = 1
    ret = 0
    t = 0
    c = 1
    for x in reversed(tuple(A)):
        t = (t + c * x) % P
        ret += ctr[t]
        ctr[t] += 1
        c = c * 10 % P
    print(ret)


def __starting_point():
    main()


__starting_point()
