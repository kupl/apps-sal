def kk():
    return map(int, input().split())


def k2():
    return map(lambda x: int(x) - 1, input().split())


def ll():
    return list(kk())


(n, ls) = (int(input()), ll())
print(2 + (ls[2] ^ min(ls)))
