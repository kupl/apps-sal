#!/usr/bin/env python3
# encoding: utf-8


# ----------
# Constants
# ----------


# ----------
# Functions
# ----------
def convert(a):
    b = list()
    toAdd = a[0]
    cnt = 1
    for item in a[1:]:
        if item == toAdd:
            cnt += 1
        else:
            b.append((toAdd, cnt))
            toAdd = item
            cnt = 1

    b.append((toAdd, cnt))
    return b


def calc(q, b):
    ans = 0
    for item in b:
        val, cnt = item
        if q >= val:
            r = q % val
            d = q // val
            if cnt < d:
                r += (d - cnt) * val
                d = cnt
            q = r
            ans += d
            if q == 0:
                break

    return ans if q == 0 else -1


# Reads a string from stdin, splits it by space chars, converts each
# substring to int, adds it to a list and returns the list as a result.
def get_ints():
    return [int(n) for n in input().split()]


# Reads a string from stdin, splits it by space chars, converts each substring
# to floating point number, adds it to a list and returns the list as a result.
def get_floats():
    return [float(n) for n in input().split()]


# ----------
# Execution start point
# ----------

def __starting_point():
    a = get_ints()
    assert len(a) == 2
    n, q = a[0], a[1]
    a = get_ints()
    assert len(a) == n
    qj = [int(input()) for i in range(q)]
    assert len(qj) == q

    a.sort()
    a.reverse()
#    print(a)
    b = convert(a)
#    print(b)

    for i in qj:
        ans = calc(i, b)
        print(ans)


__starting_point()
