#!/usr/bin/env python3
# encoding: utf-8


# ----------
# Constants
# ----------


# ----------
# Functions
# ----------

# Reads a string from stdin, splits it by space chars, converts each
# substring to int, adds it to a list and returns the list as a result.
def get_ints():
    return [int(n) for n in input().split()]


# Reads a string from stdin, splits it by space chars, converts each substring
# to floating point numbber, adds it to a list and returns the list as a result.
def get_floats():
    return [float(n) for n in input().split()]


def calc(w, rid):
    plus = True
    val = 0
    for i, t in enumerate(w):
        if i not in rid:
            if plus:
                val += t
            else:
                val -= t
            plus = not plus
    return val


# ----------
# Execution start point
# ----------

def __starting_point():
    a = get_ints()
    assert len(a) == 1
    n = a[0]
    count = 2 * n

    w = get_ints()
    assert len(w) == count
    w.sort(reverse=True)

    best = list()
    for i in range(count):
        for j in range(i + 1, count):
            best.append(calc(w, [i, j]))

    print(min(best))


__starting_point()
