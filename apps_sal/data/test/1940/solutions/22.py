import sys
import math
fin = sys.stdin
fout = sys.stdout
(n, k) = list(map(int, fin.readline().split()))
a = list(map(int, fin.readline().split()))
ans = 0
i = 0
while i < n:
    ans += math.ceil(a[i] / k)
    i += 1
fout.write(str(math.ceil(ans / 2)))
