(N, A, B) = map(int, input().split())
H = []
for _ in range(N):
    H.append(int(input()))


def is_ok(arg):
    cnt = 0
    C = A - B
    for h in H:
        wk = h - B * arg
        if wk < 0:
            continue
        else:
            cnt += (wk + C - 1) // C
    return cnt <= arg


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


ng = 0
ok = 10 ** 16
print(meguru_bisect(ng, ok))
