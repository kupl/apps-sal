from bisect import *


def solve():
    ans = 0
    N = int(input())
    A = [-int(input()) for _ in range(N)]
    lis = [A[0]]
    for i in range(1, N):
        if A[i] >= lis[-1]:
            lis.append(A[i])
        else:
            ind = bisect_right(lis, A[i])
            lis[ind] = A[i]
    ans = len(lis)
    return ans


print(solve())
