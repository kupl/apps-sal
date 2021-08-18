import sys


stdin = sys.stdin
def ns(): return stdin.readline().rstrip()
def ni(): return int(stdin.readline().rstrip())
def nm(): return list(map(int, stdin.readline().split()))
def nl(): return list(map(int, stdin.readline().split()))


def main():
    n, k = nm()
    A = [0] * (10 ** 5 + 1)
    for i in range(n):
        a, b = nm()
        A[a] += b

    sum_num = 0
    for i, a in enumerate(A):
        sum_num += a
        if sum_num >= k:
            print(i)
            return


def __starting_point():
    main()


__starting_point()
