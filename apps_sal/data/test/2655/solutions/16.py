import math


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort(reverse=True)
    A_half = math.ceil(N / 2)
    A_pre = A[:A_half]
    A_post = A[A_half:]
    ret = sum(A_pre)
    for i in range(len(A_post) - 1):
        ret += min(A_pre[i], A_pre[(i + 1) % A_half])
    print(ret)


solve()
