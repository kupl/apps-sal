from itertools import permutations as pp
from functools import reduce
try:
    s,p,k = map(int,input().split())
    x = []
    n = int(p**(0.5))+1
    for i in range(1,n):
        if p%i == 0:
            if i < s:
                x.append(i)
            if p//i < s:
                x.append(p//i)
    x = x*k
    x = list(set(pp(x,k)))
    n = len(x)
    flag = 1
    for i in x:
        if s == sum(i) and p == reduce((lambda a,b: a*b),i):
            print(*i)
            flag = 0
            break
    if flag:
        print("NO")
except:
    pass
