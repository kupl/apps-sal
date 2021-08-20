from math import sqrt


def divide_into_p(p, a):
    q = a // (p + 1)
    r = a % (p + 1)
    if r == 0:
        return q
    elif q + r >= p:
        return q + 1
    else:
        return None


def divisible_into_p(p, lst):
    lgth = 0
    for l in lst:
        dp = divide_into_p(p, l)
        if dp == None:
            return None
        else:
            lgth += dp
    return lgth


def index_lst(a, sqrta):
    lst = []
    for i in range(1, sqrta + 1):
        p = a // i
        lst.append(p)
        if not a % p:
            lst.append(p - 1)
    for i in range(sqrta + 1, 0, -1):
        lst.append(i)
    return lst


def check_all_p(balls):
    a = balls[0]
    sqrt_a = int(sqrt(a))
    indices = index_lst(a, sqrt_a)
    for i in indices:
        dp = divisible_into_p(i, balls)
        if dp != None:
            return dp


input()
balls = sorted([int(x) for x in input().split()])
print(check_all_p(balls))
