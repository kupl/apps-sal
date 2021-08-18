import sys
input = sys.stdin.readline

q = int(input())


def sortper(begin):
    x = A.index(min(A[begin:]))

    return x, A[:begin] + [A[x]] + A[begin:x] + A[x + 1:]


for testcases in range(q):
    n = int(input())
    A = list(map(int, input().split()))

    begin = 0

    while begin < n - 1:
        nbegin, A = sortper(begin)

        if begin == nbegin:
            begin += 1
        else:
            begin = nbegin

    print(*A)
