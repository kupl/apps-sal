import sys
import math
import queue
import bisect
MOD = 10 ** 9 + 7
sys.setrecursionlimit(1000000)
(n, x) = map(int, input().split())
taken = {0, x}
b = [0]
for i in range(1, 1 << n):
    if i not in taken and i ^ x not in taken:
        b.append(i)
        taken.add(i)
b = [b[i] ^ b[i - 1] for i in range(1, len(b))]
print(len(b))
print(*b)
