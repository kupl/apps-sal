from sys import stdin
from math import gcd
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
ans = arr[0]
for x in arr:
    ans = gcd(ans, x)
flag = False
for x in arr:
    flag |= x == ans
if flag:
    print(ans)
else:
    print(-1)
