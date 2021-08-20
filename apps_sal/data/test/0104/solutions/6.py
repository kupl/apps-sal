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
    n = int(input())
    a = [int(x) for x in input().split()]
    aa = sum(a)
    cc = 0
    for i in range(n):
        cc += a[i]
        if cc >= math.ceil(aa / 2):
            print(i + 1)
            break


def __starting_point():
    main()


__starting_point()
