import sys
from io import StringIO
from contextlib import contextmanager
import traceback
import time


def r(a):
    i = 0
    while not a % 2:
        a //= 2
        i += 1
    return a, i


def chem(n, A):
    p, _ = r(A[0])
    for a in A:
        q, _ = r(a)
        while p != q:
            if p > q:
                p, q = q, p
            q, _ = r(q // 2)
        if q == 1:
            break
    t = 0
    L = []
    for a in A:
        q, i = r(a)
        while q != p:
            t += i + 1
            q, i = r(q // 2)
        L.append(i)

    L.sort()
    m = (L[n // 2] + L[(n - 1) // 2]) // 2
    return t + sum(abs(l - m) for l in L)


def main():
    n = readint()
    A = readintl()
    assert len(A) == n
    print(chem(n, A))


def readint():
    return int(input())


def readinti():
    return map(int, input().split())


def readintl():
    return list(readinti())


def readintll(k):
    return [readintl() for _ in range(k)]


def log(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


@contextmanager
def patchio(i):
    try:
        sys.stdin = StringIO(i)
        sys.stdout = StringIO()
        yield sys.stdout
    finally:
        sys.stdin = sys.__stdin__
        sys.stdout = sys.__stdout__


def do_test(k, test):
    try:
        log(f"TEST {k}")
        i, o = test
        with patchio(i) as r:
            t0 = time.time()
            main()
            t1 = time.time()
        if r.getvalue() == o:
            log(f"OK ({int((t1-t0)*1000000)/1000:0.3f} ms)\n")
        else:
            log(f"Expected:\n{o}"
                f"Got ({int((t1-t0)*1000000)/1000:0.3f} ms):\n{r.getvalue()}")
    except Exception:
        traceback.print_exc()
        log()


def test(ts):
    for k in ts or range(len(tests)):
        do_test(k, tests[k])


tests = [("""\
3
4 8 2
""", """\
2
"""), ("""\
3
3 5 6
""", """\
5
""")]


def __starting_point():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--test', '-t', type=int, nargs='*')
    args = parser.parse_args()
    main() if args.test is None else test(args.test)


__starting_point()
