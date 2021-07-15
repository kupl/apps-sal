import sys
input=sys.stdin.readline
from collections import defaultdict as dc
from bisect import bisect_right
import math
for _ in range(int(input())):
    n=int(input())
    x=n%10
    c=10*(x-1)
    s=str(n)
    for i in range(len(s)):
        c+=i+1
    print(c)
