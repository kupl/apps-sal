# coding: utf-8

def check(A):
    tmp = 0
    first = A[0]
    A.pop(0)
    for i in A:
        if i < first:
            tmp += 1
    return tmp


def main():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    con = [1, 1, 2, 6, 24, 120, 720, 5040, 40320]

    a, b = 0, 0

    for i in range(N, 0, -1):
        a += con[i - 1] * check(P)
        b += con[i - 1] * check(Q)

    print((abs(a - b)))


def __starting_point():
    main()


__starting_point()
