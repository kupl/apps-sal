# 過去の提出を見ながら解いた

def main():
    N, M = list(map(int, input().split()))
    *a, = list(map(int, input().split()))
    a.sort()

    def count(mid) -> int:
        cnt = 0  # (i,j)>=mid の個数
        j = N  # j: iと組んでペア和>=midを満たすjの下限, 初期値は範囲外=条件を満たすjはない
        for i in range(N):
            while j > 0 and a[i] + a[j - 1] >= mid:
                j -= 1
            # j==0 or a[i]+a[j]>=mid
            # j==0
            # 現在のiに対しすべてのaの要素が相方になる。
            # 一度そのようなiに達したら、それ以降のiはすべてこの条件を満たす。
            cnt += N - j  # iに対し[j,N)が相方になる
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
    j = N  # j: iと組んでペア和>=midを満たすjの下限, 初期値は範囲外=条件を満たすjはない
    for i in range(N):
        while j > 0 and a[i] + a[j - 1] >= ma:
            j -= 1
        ans += a[i] * (N - j) + acc[N] - acc[j]  # i側の寄与=ペア数,j側の寄与=acc
    ans += (ma - 1) * (M - count(ma))  # ペア和maではMペア組めないが、ma-1で埋められる

    print(ans)


def __starting_point():
    main()


__starting_point()
