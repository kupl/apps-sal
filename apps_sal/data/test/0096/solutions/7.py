import sys


def minp():
    return sys.stdin.readline().strip()


def mint():
    return int(minp())


def mints():
    return list(map(int, minp().split()))


def full(x, n):
    if ((n + 1) & n) != 0:
        raise Exception("qwe")
    r = 1
    while True:
        if r >= x:
            return n
        if n == 1:
            return None
        r *= 2
        n -= 1
        if r >= x:
            return n
        n //= 2
        r += 1


def is_good(x, n):
    l = x
    r = x
    rp = x
    if x % 2 == 0:
        return None
    while l <= n:
        if l <= n and r > n:
            return None
        l *= 2
        rp = r
        r = r * 2 + 1
    return rp


def full2(x, c, rp):
    r = 1
    while True:
        if r >= x:
            return rp
        if rp == c:
            return None
        r *= 2
        rp -= 1
        if r >= x:
            return rp
        rp //= 2
        r += 1
    return None


def full1(k, x, n):
    rp = is_good(x, n)
    if rp == None:
        r = None
        if f(x, n) >= k:
            r = x
        if 2 * x <= n:
            r1 = full1(k, 2 * x, n)
            if r1 != None and (r == None or r < r1):
                r = r1
        if 2 * x + 1 <= n:
            r1 = full1(k, 2 * x + 1, n)
            if r1 != None and (r == None or r < r1):
                r = r1
        return r
    else:
        return full2(k, x, rp)


def fulls(k, n):
    r = 1
    for i in range(1, n + 1):
        if f(i, n) >= k:
            r = i
    return r


def f(x, n):
    r = 0
    rp = is_good(x, n)
    if rp != None:
        r = 1
        while rp != x:
            r = (r * 2 + 1)
            rp //= 2
        return r

    if x <= n:
        r += 1
    if x % 2 == 0 and x + 1 <= n:
        r += f(x + 1, n)
    if 2 * x <= n:
        r += f(x * 2, n)
    #print(x, r)
    return r


def f1(x, n):
    r = 0
    if x <= n:
        r += 1
    if x % 2 == 0 and x + 1 <= n:
        r += f(x + 1, n)
    if 2 * x <= n:
        r += f(x * 2, n)
    #print(x, r)
    return r


'''
from random import randint
while True:
	n = randint(1, 1024)
	x = randint(1, n)
	if full1(x, 1, n) != fulls(x, n):
		print(x, n, full1(x, 1, n), fulls(x,n))
'''
n, k = mints()
print(full1(k, 1, n))
