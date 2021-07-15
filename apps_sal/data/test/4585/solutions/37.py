import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    x = ni()
    d = 0
    for i in range(1, x + 1):
        d += i
        if d >= x:
            print(i)
            return


def __starting_point():
    main()

__starting_point()
