def solve(x):
    """
    二分探索で使用する条件
    :param x:
    :return:
    """
    return A * x + B * len(str(x)) <= X


def binary_search(ok, ng):
    """
    半開区間を用いることでバグがおきにくいようにしている。
    okを解が存在する値、ngに解が存在しない値を入れる。最大値も最小値の探索を行うことも出来る。
    [ok, ng) or (ng, ok]
    ok = 10 ** 9
    ng = -1

    :param ok:解が存在する境界値
    :param ng:解が存在しない境界値
    :return:
    """
    while abs(ok - ng) > 1:
        middle = (ok + ng) // 2
        if solve(middle):
            ok = middle
        else:
            ng = middle
    return ok


(A, B, X) = map(int, input().split())
ans = binary_search(0, 10 ** 9 + 1)
print(ans)
