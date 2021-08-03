import math
from collections import defaultdict
def ml(): return map(int, input().split())
def ll(): return list(map(int, input().split()))
def ii(): return int(input())
def ip(): return input()


"""========main code==============="""

t = ii()
for _ in range(t):
    x = ii()
    a = ll()
    b = ll()
    one = -1
    minus = -1
    f = 0
    for i in range(x):
        if(b[i] > a[i]):
            if(one == -1):
                f = 1
                break
        elif (b[i] < a[i]):
            if(minus == -1):
                f = 1
                break
        if(a[i] == 1):
            one = 1
        elif(a[i] == -1):
            minus = 1
    if(f):
        print("NO")
    else:
        print("YES")
