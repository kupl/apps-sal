import sys
import math
MOD = 998244353
for i in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    z = a.count(0)
    s = sum(a)
    ans = z + (s + z == 0)
    print(ans)
