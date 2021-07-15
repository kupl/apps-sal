import sys
from fractions import gcd
from itertools import groupby as gb
from itertools import permutations as perm
from collections import Counter as C
from collections import defaultdict as dd
sys.setrecursionlimit(10**5)

mod = 998244353
n = int(input())
s = input()
if s == s[0]*n:
    print(n*(n+1)//2)
    return
g = gb(s)
gg = gb(s[::-1])
a = 0
a_c,b_c = '',''
b = 0
for k,v in g:
    a = len(list(v))
    a_c = k
    break
for k,v in gg:
    b = len(list(v))
    b_c = k
    break
res = 0
if a_c == b_c:
    res += a * b
res += a + b + 1
print(int(res)%mod)

