import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    a, b = nm()
    print((sum(range(1, b - a)) - a))


def __starting_point():
    main()


__starting_point()
