def r():
    return input()


def ri():
    return int(r())


def rr():
    return map(int, r().split())


def rl():
    return list(rr())


n = ri()
a = rl()
if 1 in a:
    print(-1)
else:
    print(1)
