import atexit
import io
import sys

# Buffering IO
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


def main():
    n, k, m = [int(x) for x in input().split()]
    s = input().split()
    mm = {}
    a = [int(x) for x in input().split()]
    group = []
    for i in range(k):
        ii = [int(x) - 1 for x in input().split()][1:]
        mc = min(a[x] for x in ii)
        for iii in ii:
            mm[s[iii]] = mc

    print(sum(mm[x] for x in input().split()))


def __starting_point():
    main()


__starting_point()
