import bisect


def getIntList(lst):
    assert type(lst) is list
    rep = []
    for i in lst:
        rep.append(int(i))
    return rep


n, k, A, B = getIntList(input().split())
pos = getIntList(input().split())


def calc(l, r, heros):
    assert type(heros) is list
    if len(heros) == 0:
        return A
    if r - l == 0:
        return B * len(heros)
    mid = bisect.bisect_right(heros, (l + r) // 2)
    tans = min(
        calc(l, (l + r) // 2, heros[:mid]) + calc((l + r) // 2 + 1, r, heros[mid:]),
        B * len(heros) * (r - l + 1)
    )
    return tans


pos.sort()
ans = calc(1, 2**n, pos)
print(ans)
