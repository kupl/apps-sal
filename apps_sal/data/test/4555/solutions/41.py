import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    a, b, k = nm()

    for i in range(a, min(a + k, b + 1)):
        print(i)
    for i in range(max(a + k, b - k + 1), b + 1):
        print(i)


def __starting_point():
    main()


__starting_point()
