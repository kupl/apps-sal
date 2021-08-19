import sys
from collections import deque

import bisect


def input():
    return sys.stdin.readline().rstrip()


def main():
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    A.sort()

    #    print(A)
    pp = int(bisect.bisect_left(A, 0))
    A_minus = deque(A[:pp])
    A_plus = deque(A[pp:])

    AA = deque([])
    AAm = deque([])
    if N == K:
        ans = 1
        for i in A:
            ans *= i
            ans %= mod
        print((ans % mod))

    elif K % 2 == 0:
        ans = 1

        while len(A_minus) >= 2:
            a1 = A_minus.popleft()
            a2 = A_minus.popleft()
            AAm.append(a1 * a2)

        while len(A_plus) >= 2:
            a1 = A_plus.pop()
            a2 = A_plus.pop()
            AA.append(a1 * a2)

        for i in range(K // 2):
            if len(AAm) == 0:
                temp = AA.popleft()
            elif len(AA) == 0:
                temp = AAm.popleft()
            elif AAm[0] > AA[0]:
                temp = AAm.popleft()
            else:
                temp = AA.popleft()
            ans *= temp
            ans %= mod
        print((ans % mod))

    elif len(A_plus) == 0:
        ans = 1
        for i in range(K):
            ans *= A_minus.pop()
            ans %= mod
        print((ans % mod))

    else:
        ans = A_plus.pop()

        while len(A_minus) >= 2:
            a1 = A_minus.popleft()
            a2 = A_minus.popleft()
            AAm.append(a1 * a2)

        while len(A_plus) >= 2:
            a1 = A_plus.pop()
            a2 = A_plus.pop()
            AA.append(a1 * a2)

        for i in range(K // 2):
            if len(AAm) == 0:
                temp = AA.popleft()
            elif len(AA) == 0:
                temp = AAm.popleft()
            elif AAm[0] > AA[0]:
                temp = AAm.popleft()
            else:
                temp = AA.popleft()
            ans *= temp
            ans %= mod
        print((ans % mod))


def __starting_point():
    main()


__starting_point()
