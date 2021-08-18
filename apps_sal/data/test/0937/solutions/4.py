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
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    t = [int(x) for x in input().split()]

    mx = 0
    for i in range(n):
        if i < k:
            mx += a[i]
        else:
            mx += a[i] * t[i]

    xx = mx
    for i in range(n):
        if i + k >= n:
            break
        xx -= a[i]
        xx += a[i] * t[i]
        xx += a[i + k]
        xx -= a[i + k] * t[i + k]
        mx = max(xx, mx)

    print(mx)


def __starting_point():
    main()


__starting_point()
