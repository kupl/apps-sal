import sys
import math
import sys
import math
(n, m) = [int(x) for x in sys.stdin.readline().split()]
st = sys.stdin.readline()
res = 0
i = 0
vi = 0
while i < n:
    if st[vi] == '-':
        res += 1
        vi += 3
    else:
        vi += 2
    i += 1
vmin = min(res, n - res)
vmin *= 2
for i in range(m):
    (l, r) = [int(x) for x in sys.stdin.readline().split()]
    k = r - l + 1
    if k % 2 != 0:
        sys.stdout.write('0\n')
    elif k <= vmin:
        sys.stdout.write('1\n')
    else:
        sys.stdout.write('0\n')
