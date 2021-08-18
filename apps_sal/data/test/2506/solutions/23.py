
def main():
    N, M = list(map(int, input().split()))
    *a, = list(map(int, input().split()))
    a.sort()

    def count(mid) -> int:
        cnt = 0
        j = N
        for i in range(N):
            while j > 0 and a[i] + a[j - 1] >= mid:
                j -= 1
            cnt += N - j
        return cnt

    def binary_search(*, ok: int, ng: int, is_ok: 'function') -> int:
        """あるペア和以上のみ採用する場合に
        M回以上握手できないようなペア和の上限"""
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if is_ok(mid):
                ok = mid
            else:
                ng = mid
        return ok

    ma = binary_search(ok=2 * 10 ** 5 + 1, ng=0, is_ok=lambda mid: count(mid) < M)

    def accumulate(a):
        s = 0
        yield s
        for x in a:
            s += x
            yield s

    *acc, = accumulate(a)

    ans = 0
    j = N
    for i in range(N):
        while j > 0 and a[i] + a[j - 1] >= ma:
            j -= 1
        ans += a[i] * (N - j) + acc[N] - acc[j]
    ans += (ma - 1) * (M - count(ma))

    print(ans)


def __starting_point():
    main()


__starting_point()
