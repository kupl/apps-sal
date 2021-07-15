import sys,math,collections,itertools
input = sys.stdin.readline

N=int(input())
s = []
if N ==0:
    print((0))
    return
    
while N:
    r = N%(-2)
    if r<0:
        r+=2
    N = (N-r)//(-2)
    s.append(str(r))

print((''.join(s)[::-1]))

