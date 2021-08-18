import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main():
    n, m = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    print(min(c.count(x) for x in range(1, n + 1)))


def __starting_point():
    main()


__starting_point()
