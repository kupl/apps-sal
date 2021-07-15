#!/usr/bin/env python3
# encoding: utf-8



#----------
# Constants
#----------
LEFT = 0
RIGHT = 1



#----------
# Functions
#----------

# Reads a string from stdin, splits it by space chars, converts each
# substring to int, adds it to a list and returns the list as a result.
def get_ints():
    return [ int(n) for n in input().split() ]



#----------
# Execution start point
#----------

def __starting_point():
    import sys

    a = get_ints()
    assert len(a) == 1
    n = a[0]

    links = [ set() for i in range(n) ]
    for i in range(n-1):
        a = get_ints()
        assert len(a) == 2
        for j in range(2):
            a[j] -= 1
        links[a[0]].add(a[1])
        links[a[1]].add(a[0])

    count = [ 0, 0 ]
    looked = [ False for i in range(n) ]
    stack = dict()
    stack[0] = LEFT
    while stack:
        index, side = stack.popitem()
        if not looked[index]:
            looked[index] = True
            count[side] += 1
            for i in links[index]:
                stack[i] = 1 - side

    res = count[LEFT] * count[RIGHT] - n + 1
    print("%d" % res)

__starting_point()
