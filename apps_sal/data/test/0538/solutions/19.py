#!/usr/bin/env python3
# encoding: utf-8



#----------
# Constants
#----------



#----------
# Functions
#----------

# Reads a string from stdin, splits it by space chars, converts each
# substring to int, adds it to a list and returns the list as a result.
def get_ints():
    return [ int(n) for n in input().split() ]


# Reads a string from stdin, splits it by space chars, converts each substring
# to floating point numbber, adds it to a list and returns the list as a result.
def get_floats():
    return [ float(n) for n in input().split() ]


#----------
# Execution start point
#----------

def __starting_point():
    a = get_ints()
    assert len(a) == 1
    x = a[0]

    s = str(x).rstrip('0')
    print("YES" if s == s[::-1] else "NO")

__starting_point()
