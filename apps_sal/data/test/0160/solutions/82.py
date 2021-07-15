import sys
from itertools import accumulate
N, K = list(map(int, input().split()))
*A, = list(map(int, input().split()))
S = sum(A)

div_small = []
div_large = []
for p in range(1, int(S**0.5)+1):
    if S % p == 0:
        div_small.append(p)
        if S // p != p:
            div_large.append(S//p)
div_large += div_small[::-1]

for d in div_large:
    R = sorted([a % d for a in A])
    SR = sum(R)
    acc = tuple(accumulate(R))

    for i, l in enumerate(acc):
        r = d*(N-i-1)-(SR-l)
        if l == r:
            if l <= K:
                print(d)
                return
            else:
                break

