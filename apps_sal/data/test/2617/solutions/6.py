from itertools import accumulate
import sys
input = sys.stdin.readline


PLUS = [1 << i for i in range(1, 31)]
SUM = list(accumulate(PLUS))

t = int(input())
for tests in range(t):
    n = int(input()) - 1

    for i in range(30):
        if SUM[i] >= n:
            ANS = i + 1
            break
    print(ANS)
    ALIST = [0] * ANS
    NOW = 1
    n -= ANS

    for i in range(ANS):
        ALIST[i] = min(n // (ANS - i), NOW)
        n -= ALIST[i] * (ANS - i)
        NOW += ALIST[i]
        # print(n,ALIST,NOW)
    print(*ALIST)
