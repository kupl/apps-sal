# BubbleCup 12 - C

import math

L = int(input())
A = input()

f = int("".join(A[:L]))
tn = False
if (1 - abs((math.log(f + 1) / math.log(10)) % 1)) % 1 < (10 ** -9):
    tn = True
if len(A) % L != 0:
    ln = len(A) + (L - len(A) % L)
    num = ("1" + "0" * (L - 1)) * (ln // L)
    print(num)
else:
    f = int("".join(A[:L]))
    fn = False
    ft = True
    for i in range(L, len(A), L):
        if int("".join(A[i:i + L])) > f and not fn:
            ft = False
        if int("".join(A[i:i + L])) < f:
            fn = True
    if fn and ft:
        print(str(f) * (len(A) // L))
    elif tn:
        print(("1" + "0" * (L - 1)) * ((len(A) // L) + 1))
    else:
        print(str(f + 1) * (len(A) // L))
