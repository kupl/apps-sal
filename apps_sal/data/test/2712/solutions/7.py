import sys
reader = (s.rstrip() for s in sys.stdin)
input = reader.__next__


def gift():
    for _ in range(t):
        a, b, c = list(map(int, input().split()))
        yield a + b + c - 1


def __starting_point():
    t = int(input())
    ans = gift()
    print(*ans, sep='\n')


__starting_point()
