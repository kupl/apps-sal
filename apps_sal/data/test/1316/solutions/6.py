import copy
import itertools
import string


def powmod(x, p, m):
    if p <= 0:
        return 1
    if p <= 1:
        return x % m
    return powmod(x * x % m, p // 2, m) * (x % m)**(p % 2) % m


def to_basex(num, x):
    while num > 0:
        yield num % x
        num //= x


def from_basex(it, x):
    ret = 0
    p = 1
    for d in it:
        ret += d * p
        p *= x
    return ret


def core():
    n, k = (int(x) for x in input().split())
    s = input()

    ansd = {l: 0 for l in string.ascii_lowercase}
    for l in string.ascii_lowercase:
        cnt = 0
        for ch in s:
            if ch == l:
                cnt += 1
                if cnt >= k:
                    ansd[l] += 1
                    cnt = 0
            else:
                cnt = 0

    ans = max(ansd.values())
    print(ans)


core()
