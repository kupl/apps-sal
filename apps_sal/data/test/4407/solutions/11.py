#!/usr/bin/env python3
# encoding: utf-8



#----------
# Constants
#----------

DEGREE_ARRAY_SIZE = 32
VALUES = { 2**i: i for i in range(DEGREE_ARRAY_SIZE) }

#----------
# Functions
#----------
def convert(a):
    from collections import Counter
    b = [ 0 for i in range(DEGREE_ARRAY_SIZE) ]
    total = 0
    for val, cnt in list(Counter(a).items()):
        b[VALUES[val]] += cnt
        total += cnt * val
    start = 0
    for i, cnt in enumerate(reversed(b)):
        if cnt != 0:
            start = DEGREE_ARRAY_SIZE - i
            break
    return b, total, start


def calc(q, b):
    ans = 0
    val = 2 ** (len(b) - 1)
    for cnt in reversed(b):
        if q >= val:
            c = min(cnt, q // val)
            q -= c * val
            ans += c
            if q == 0:
                break
        val //= 2

    return ans if q == 0 else -1


# Reads a string from stdin, splits it by space chars, converts each
# substring to int, adds it to a list and returns the list as a result.
def get_ints():
    return [ int(n) for n in input().split() ]


# Reads a string from stdin, splits it by space chars, converts each substring
# to floating point number, adds it to a list and returns the list as a result.
def get_floats():
    return [ float(n) for n in input().split() ]


#----------
# Execution start point
#----------

def __starting_point():
    a = get_ints()
    assert len(a) == 2
    n, q = a[0], a[1]
    a = get_ints()
    assert len(a) == n
    qj = [int(input()) for i in range(q)]
    assert len(qj) == q

    b, total, start = convert(a)
    b = b[:start]
    assert sum(b) == n

    DEGREE_ARRAY_SIZE = start

    for i in qj:
        if i < total:
            ans = calc(i, b)
        elif i == total:
            ans = n
        else:
            ans = -1
        print(ans)

__starting_point()
