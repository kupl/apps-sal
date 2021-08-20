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
    n = input()
    mm = 0
    for i in range(1, 2 ** len(n)):
        x = ''
        for c in range(len(n)):
            if i % 2:
                x += n[c]
            i = i // 2
        if x[0] == '0':
            continue
        xx = int(x)
        if int(xx ** 0.5) ** 2 == xx:
            if len(x) > mm:
                mm = len(x)
    print(len(n) - mm if mm > 0 else -1)


def __starting_point():
    main()


__starting_point()
