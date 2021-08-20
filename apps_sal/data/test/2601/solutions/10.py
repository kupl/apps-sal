import sys


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(a) for a in input().split()]
    for i in range(N - 1):
        if A[i] <= A[i + 1]:
            print('YES')
            break
    else:
        print('NO')
