def binary_search(*, ok, ng, is_ok):
    while abs(ok - ng) > 1:
        mid = (ng + ok) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    from itertools import accumulate

    N, M = list(map(int, input().split()))
    *A, = sorted(map(int, input().split()))

    acc = [0]
    for x in accumulate(A):
        acc.append(x)

    def count(h):
        ret = 0

        j = N
        for i in range(N):
            while j - 1 >= 0 and A[i] + A[j - 1] >= h:
                j -= 1
            ret += N - j
            # [j,N)の要素数

        return ret

    x = binary_search(ok=A[-1] * 2 + 1, ng=0, is_ok=lambda x: count(x) < M)
    # 幸福度の総和がX以上のペア数がM未満となる最大のX

    s = 0
    j = N
    for i in range(N):
        while j - 1 >= 0 and A[i] + A[j - 1] >= x:
            j -= 1
        s += A[i] * (N - j) + acc[N] - acc[j]
    s += (M - count(x)) * (x - 1)

    print(s)


def __starting_point():
    main()


__starting_point()
