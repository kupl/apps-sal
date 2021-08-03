import sys
import math
n, k = list(map(int, sys.stdin.readline().split()))
arr = list(map(int, sys.stdin.readline().split()))
ans = 1
for i in arr:
    ans = math.gcd(k, i * ans // math.gcd(i, ans))
if ans == k:
    print('Yes')
else:
    print('No')
