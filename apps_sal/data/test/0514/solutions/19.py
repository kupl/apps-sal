import math


def inp(dtype=str, strip=True):
    s = input()
    res = [dtype(p) for p in s.split()]
    res = res[0] if len(res) == 1 and strip else res
    return res


def problem1():
    t = inp(int)
    for _ in range(t):
        n, d = inp(int)
        res = False
        sq = math.floor(math.sqrt(d))
        for x in range(max(sq - 1000, 0), min(sq + 1000, n)):
            if x + math.ceil(d / (x + 1)) <= n:
                res = True
                break
        if res:
            print('YES')
        else:
            print('NO')


def problem2():
    pass


def problem3():
    pass


def problem4():
    pass


def problem5():
    pass


def problem6():
    pass


def __starting_point():
    # problem6()
    # problem5()
    # problem4()
    # problem3()
    # problem2()
    problem1()

__starting_point()
