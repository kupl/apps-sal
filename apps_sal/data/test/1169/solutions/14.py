import os
import sys

n, m = [int(num) for num in sys.stdin.readline().split()]

# for _ in range(t):
#     s, a, b, c = [int(s) for s in sys.stdin.readline().split()]
#     s = s // c
#     res = (a + b) * (s // a) + s % a
#     sys.stdout.write("{0}\n".format(res))

res1 = max([0, n - 2 * m])
res2 = 0
while res2 * (res2 - 1) < (2 * m):
    res2 += 1

print(res1, n - res2)

