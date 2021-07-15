#!/usr/bin/env python3
# encoding: utf-8



#----------
# Constants
#----------

DEGREE_ARRAY_SIZE = 32

#----------
# Functions
#----------
def convert(a):
    from collections import Counter
    b = [ 0 for i in range(DEGREE_ARRAY_SIZE) ]
    for val, cnt in list(Counter(a).items()):
        b[val.bit_length()-1] += cnt
    start = 0
    for i, cnt in enumerate(reversed(b)):
        if cnt != 0:
            start = DEGREE_ARRAY_SIZE - i
            break
    return b, start


def calc(q, b):
    ans = 0
    val_power = (len(b) - 1)
    for cnt in reversed(b):
        c = min(cnt, q >> val_power)
        q -= c * (1 << val_power)
        ans += c
        #if q == 0:
        #    break
        val_power -= 1

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

    b, start = convert(a)
#    print(str(b))
#    print(total)
    b = b[:start]
    DEGREE_ARRAY_SIZE = start
#    print(str(b))

    q = [int(input()) for _ in range(q)]
    for i in q:
        ans = calc(i, b)
        print(ans)

__starting_point()
