import sys
import math
f = sys.stdin
out = sys.stdout


def lPowOf2leqn(n):
    n = n | n >> 1
    n = n | n >> 2
    n = n | n >> 4
    n = n | n >> 8
    n = n | n >> 16
    return n + 1 >> 1


n = int(f.readline().rstrip('\r\n'))
out.write(str(int(math.log2(lPowOf2leqn(n))) + 1) + '\n')
