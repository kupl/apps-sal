import sys
import time
import heapq
import collections
from io import StringIO
test_cases = [('\n3 5\nabc\nxaybz\n', '\n2\n2 3 \n'), ('\n4 10\nabcd\nebceabazcd\n', '\n1\n2 \n')]


def solve():
    return 'TEST'


def debug(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def main():
    (n, m) = map(int, input().split())
    s = input()
    t = input()
    min_diff = None
    for i in range(m - n + 1):
        diff = [k + 1 for (k, c) in enumerate(s) if c != t[k + i]]
        if min_diff is None or len(diff) < len(min_diff):
            min_diff = diff
    print(len(min_diff))
    print(' '.join((str(i) for i in min_diff)))


def test(s, check):
    s = s.strip()
    check = check.strip()
    sys.stdin = StringIO(s)
    sys.stdout = out = StringIO()
    start_time = time.time()
    try:
        main()
    finally:
        exec_time = time.time() - start_time
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__
    out.seek(0)
    result = out.read().strip()
    status = 'SUCCESS' if result == check else 'FAILURE'
    message = 'status: {}, exec_time: {:.3f}'.format(status, exec_time)
    debug(message)


def test_all():
    for (s, check) in test_cases:
        test(s, check)


def __starting_point():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        test_all()
    else:
        main()


__starting_point()
