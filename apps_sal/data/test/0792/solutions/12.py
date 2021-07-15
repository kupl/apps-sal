import os
import sys

def log(*args, **kwargs):
    if os.environ.get('CODEFR'):
        print(*args, **kwargs)


#n = int(input())
n, d = tuple(map(int,input().split()))
a = list(map(int,input().split()))

s = 0
k = 0
dep = 0
for i in a:
    if i == 0:
        if s < 0:
            if dep < -s:
                k += 1
                dep = d
            else:
                dep += s
            s = 0
    else:
        s += i
        if s > d:
            print(-1)
            return
        dep = min(dep, d - s)

print(k)

