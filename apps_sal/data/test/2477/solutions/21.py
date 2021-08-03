N, K = map(int, input().split())
A = list(map(int, input().split()))


def is_ok(mid):
    x = 0
    for a in A:
        x += -(-a // mid) - 1
    if x <= K:
        return True
    return False


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


print(meguru_bisect(0, max(A)))
