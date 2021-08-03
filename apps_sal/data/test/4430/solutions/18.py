import math
import sys
n, m, k = map(int, sys.stdin.readline().split())
a = [int(x) for x in sys.stdin.readline().split()]
a.reverse()
ans = 0
bag = m - 1
size = k
for x in a:
    if size < x:
        if bag > 0:
            bag -= 1
            size = k - x
        else:
            break
    else:
        size -= x
    ans += 1
sys.stdout.write(str(ans))
