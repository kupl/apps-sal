import sys


def main():
    N, M = tuple(map(int, sys.stdin.readline().split()))
    if M % 2 == 1:
        m1, m2 = M // 2, M // 2 + 1
        for i in range(m1):
            l, r = i + 1, M - i
            print(str(l) + ' ' + str(r))
        for i in range(m2):
            l, r = M + 1 + i, 2 * M + 1 - i
            print(str(l) + ' ' + str(r))
    else:
        m = M // 2
        for i in range(m):
            l, r = i + 1, M + 1 - i
            print(str(l) + ' ' + str(r))
        for i in range(m):
            l, r = M + 2 + i, 2 * M + 1 - i
            print(str(l) + ' ' + str(r))


def __starting_point(): main()


__starting_point()
