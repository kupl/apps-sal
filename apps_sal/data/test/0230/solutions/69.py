import sys


def input():
    return sys.stdin.readline().rstrip()


def is_ok(arg, S):
    dic = {}
    ans = False
    for i in range(len(S) - arg + 1):
        c = S[i:i + arg]
        if c in dic:
            if i - dic[c] >= arg:
                ans = True
                break
        else:
            dic[c] = i
    return ans


def meguru_bisect(ng, ok, S):
    """
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    """
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if is_ok(mid, S):
            ok = mid
        else:
            ng = mid
    return ok


def main():
    N = int(input())
    S = input()
    print(meguru_bisect(N // 2 + 1, -1, S))


def __starting_point():
    main()


__starting_point()
