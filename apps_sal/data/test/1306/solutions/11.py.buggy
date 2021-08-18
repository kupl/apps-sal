
from collections import defaultdict

import sys

d = defaultdict(int)

#input = raw_input

N, h = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

B = [0]
for a in A:
    B.append(h - a)
    if h - a < 0:
        print(0)
        return
B.append(0)

MOD = 10**9 + 7

d[0, False, False] = 1

for i in range(1, N + 2):
    for op in [False, True]:
        for cl in [False, True]:
            last_close = B[i - 1] - B[i] + int(op)
            #
            if cl and B[i] == 0:
                continue  # can't close anything
            if last_close not in [0, 1]:
                continue  # doesn't add up
            s = d[i - 1, False, bool(last_close)] + d[i - 1, True, bool(last_close)]
            if cl:
                s *= B[i]
            # if i == 2 and op:
            #    print(cl, s, last_close,
            #          d[i-1, False, bool(last_close)] ,
            #          d[i-1, True, bool(last_close)])
            d[i, op, cl] = s % MOD

# print(d)

# for i in range(N+2):
#    print("\n", i, end=": ")
#    for op in [False, True]:
#        for cl in [False, True]:
#            print(d[i, op, cl], end=" ")
# print()


print(d[N + 1, False, False])
