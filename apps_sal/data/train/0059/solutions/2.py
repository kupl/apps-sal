import sys
input = sys.stdin.readline

t = int(input())
for test in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    MAX = 0
    DIFMIN = 10**10
    DIFMAX = -100

    for i in range(1, n):
        if A[i - 1] == A[i] == -1:
            continue
        elif A[i - 1] == -1:
            DIFMIN = min(DIFMIN, A[i])
            DIFMAX = max(DIFMAX, A[i])
        elif A[i] == -1:
            DIFMIN = min(DIFMIN, A[i - 1])
            DIFMAX = max(DIFMAX, A[i - 1])
        else:
            MAX = max(MAX, abs(A[i] - A[i - 1]))

    if DIFMIN == 10**10:
        print(0, 0)
    else:
        # print(DIFMIN,DIFMAX)
        k = (DIFMAX + DIFMIN) // 2
        m = max(MAX, DIFMAX - k, k - DIFMIN)

        print(m, k)
