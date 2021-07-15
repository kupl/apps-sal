import sys
from collections import Counter
N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

C = Counter(A)
C = sorted(C.items(), key=lambda x: x[0])
if N % 2 == 0:
    s = 1
    for k, v in C:
        if k != s or v != 2:
            print(0)
            return
        s += 2
    print(pow(2, (N // 2), MOD))
else:
    s = 0
    for k, v in C:
        if k == 0:
            if k != 0 or v != 1:
                print(0)
                return
            s += 2
            continue
        if k != s or v != 2:
            print(0)
            return
        s += 2
    print(pow(2, (N - 1) // 2, MOD))
