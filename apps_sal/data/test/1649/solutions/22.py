import sys
INF = 1 << 60
MOD = 10 ** 9 + 7
sys.setrecursionlimit(2147483647)


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    A = list(map(int, input().split()))
    A.sort()
    if sum(A[:3]) == A[3]:
        print('Yes')
    elif A[0] + A[3] == A[1] + A[2]:
        print('Yes')
    else:
        print('No')


resolve()
