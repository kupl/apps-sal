import atexit
import io
import sys
import math

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main():
    n, a, b = [int(x) for x in input().split()]
    s = input()

    if a < b:
        a, b = b, a
    cc = 0
    tt = 0
    for c in s:
        if c == '.':
            cc += 1
        else:
            aa = math.ceil(cc / 2)
            bb = math.floor(cc / 2)
            tt += min(aa, a) + min(bb, b)
            a = max(a - aa, 0)
            b = max(b - bb, 0)
            if a < b:
                a, b = b, a
            cc = 0
    aa = math.ceil(cc / 2)
    bb = math.floor(cc / 2)
    tt += min(aa, a) + min(bb, b)
    a = max(a - aa, 0)
    b = max(b - bb, 0)

    print(tt)


def __starting_point():
    main()


__starting_point()
