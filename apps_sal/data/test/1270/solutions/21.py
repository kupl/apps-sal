import math,sys,re,itertools,pprint,collections,copy
rs,ri,rai,raf=input,lambda:int(input()),lambda:list(map(int, input().split())),lambda:list(map(float, input().split()))

n = ri()

if n % 2 == 0:
    res = [2] * (n//2)
else:
    k = n - 3
    res = [3] + ([2] * (k//2))

print(len(res))
print(" ".join(map(str, res)))

