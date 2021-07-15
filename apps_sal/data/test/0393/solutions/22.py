"""Problem A - Row.

http://codeforces.com/contest/982/problem/0

You're given a row with `n` chairs. We call a seating of people "maximal" if
the two following conditions hold:

1. There are no neighbors adjacent to anyone seated.

2. It's impossible to seat one more person without violating the first rule.

The seating is given as a string consisting of zeros and ones (`0` means that
the corresponding seat is empty, `1` — occupied). The goal is to determine
whether this seating is "maximal".

Note that the first and last seats are not adjacent (if `n != 2`).

Input:

The first line contains a single integer `n` (`1 \leq n \leq 1000`) — the
number of chairs.

The next line contains a string of `n` characters, each of them is either zero
or one, describing the seating.

Output:

Output "Yes" (without quotation marks) if the seating is "maximal". Otherwise
print "No".

You are allowed to print letters in whatever case you'd like (uppercase or
lowercase).

"""
import logging


fmt = '%(levelname)s - %(name)s (line:%(lineno)s) - %(message)s'
formatter = logging.Formatter(fmt)

ch = logging.StreamHandler()
ch.setLevel(logging.NOTSET)
ch.setFormatter(formatter)

logger = logging.getLogger('row')
logger.setLevel(logging.NOTSET)
logger.addHandler(ch)


def solve(s):
    if len(s) == 1 and s == '0':
        return False  # Its possible to seat someone
    elif len(s) == 1 and s == '1':
        return True
    elif len(s) == 2 and '1' in s and '0' in s:
        return True  # maximal
    if '11' in s:
        return False
    if '000' in s or s[:2] == '00' or s[-2:] == '00':
        return False  # Its possible to seat someone
    # raise 'Missing something?'
    return True


def main():
    _ = input()
    s = input()
    result = solve(s)
    print('Yes' if result else 'No')


def __starting_point():
    main()

__starting_point()
