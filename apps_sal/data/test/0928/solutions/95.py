(N, K) = map(int, input().split())
A = list(map(int, input().split()))
S = [0] * (N + 1)
idx = -1
for i in range(N):
    S[i + 1] = S[i] + A[i]
    if idx == -1 and K <= S[i + 1]:
        idx = i + 1
if idx == -1:
    print(0)
else:
    ans = 0
    for i in range(idx, N + 1):
        excess = S[i] - K

        def is_ok(arg):
            return excess < S[arg]

        def meguru_bisect(ng, ok):
            """
            初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
            まずis_okを定義すべし
            ng ok は  とり得る最小の値-1 とり得る最大の値+1
            最大最小が逆の場合はよしなにひっくり返す
            """
            while abs(ok - ng) > 1:
                mid = (ok + ng) // 2
                if is_ok(mid):
                    ok = mid
                else:
                    ng = mid
            return ok
        ans += meguru_bisect(-1, N + 1)
    print(ans)
