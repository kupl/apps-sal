import sys
a,b=map(str,input().split())

c=a+b
c=int(c)

for i in range(c//2):
    if c==i**2:
        print('Yes')
        return

print('No')
