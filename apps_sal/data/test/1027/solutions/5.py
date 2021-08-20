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


def f(a, i):
    t = a[i]
    a[i] = 0
    for j in range(14):
        a[j] += t // 14
    for j in range(t % 14):
        a[(i + j + 1) % 14] += 1
    return sum((x for x in a if x % 2 == 0))


def main():
    a = [int(x) for x in input().split()]
    scr = 0
    for i in range(14):
        aa = a[:]
        scr = max(scr, f(aa, i))
    print(scr)


def __starting_point():
    main()


__starting_point()
