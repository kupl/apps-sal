def main():
    from collections import deque
    from operator import itemgetter
    import sys
    input = sys.stdin.readline

    MOD = 998244353

    N = int(input())

    xds = []
    xs = []
    for _ in range(N):
        x, d = list(map(int, input().split()))
        xds.append((x, d))
        xs.append(x)

    xds.sort(key=itemgetter(0), reverse=True)
    xs.sort()

    ps = [-1] * (N + 1)
    cands = deque()  # 既出の頂点で有向辺の行き先に設定されていないもの,x昇順
    for j, (x, d) in enumerate(xds):
        j = N - 1 - j
        while cands:
            cx, ci = cands[0]
            if x + d <= cx:
                # candは独立
                break
            elif x <= cx < x + d:
                # candと連結
                ps[ci] = j
                cands.popleft()
        cands.appendleft((x, j))

    ret = 1
    ctr = [1] * N
    for j, (x, d) in enumerate(xds):
        j = N - 1 - j
        par = ps[j]
        ctr[j] += 1  # j=off,子の総積が設定されている->j=on=1を加算
        if ~par:
            ctr[par] = ctr[par] * ctr[j] % MOD
        else:
            ret = ret * ctr[j] % MOD  # j=木のroot

    print(ret)
    return


def __starting_point():
    main()

__starting_point()
