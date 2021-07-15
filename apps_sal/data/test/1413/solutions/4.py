import math
import bisect

def argsort(ls):
    return sorted(range(len(ls)), key=ls.__getitem__)

def f(p=0):
    if p==0:
        return int(input())
    if p==1:
        return map(int, input().split())
    elif p==2:
        return list(map(int, input().split()))
    else:
        return sorted(list(map(int, input().split())))


n = f()
s = input()
sm = 0
for i in range(n):
    if int(s[i])%2==0:
        sm+=i+1

print(sm)
