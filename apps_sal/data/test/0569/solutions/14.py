__author__ = 'Utena'
n=int(input())
s=input()
t=0
now=set()
if n>26:print(-1)
else:
    for a in s:
        if a in now:
            t+=1
        else:
            now.add(a)
    print(t)
