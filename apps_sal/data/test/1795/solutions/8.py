import sys
import math
f = sys.stdin
n = int(f.readline())
l = list(map(int, f.readline().split()))
l = [x - 1 for x in l]
found = False
for i in range(n):
    if l[i] != i and l[l[i]] != i and (l[l[i]] != l[i]) and (l[l[l[i]]] == i):
        found = True
        print('YES')
        break
if not found:
    print('NO')
