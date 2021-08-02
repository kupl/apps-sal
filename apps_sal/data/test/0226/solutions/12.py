def maximum_pie_consumption(pies):
    c = len(pies) - 1
    toke = wait = 0
    for p in reversed(pies):
        if toke < p + wait:
            toke, wait = wait + p, toke
        else:
            wait += p
    return wait, toke


def __starting_point():
    input()
    pies = list(map(int, input().strip().split()))
    print(" ".join(map(str, maximum_pie_consumption(pies))))


__starting_point()
