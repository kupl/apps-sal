import numpy as np
import sys
def input(): return sys.stdin.readline().rstrip()


sys.setrecursionlimit(max(1000, 10**9))
def write(x): return sys.stdout.write(x + "\n")


x, y, z, K = list(map(int, input().split()))
a = np.array(list(map(int, input().split())), dtype=np.int64)
b = np.array(list(map(int, input().split())), dtype=np.int64)
c = np.array(list(map(int, input().split())), dtype=np.int64)
ab = (a + b.reshape(-1, 1)).reshape(-1)
ab.sort()
c.sort()
abk = ab[-K:]
ck = c[-K:]
l = (abk + ck.reshape(-1, 1)).reshape(-1)
l.sort()
l = l[::-1]
write("\n".join(map(str, l[:K])))
