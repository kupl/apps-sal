import sys
n=int(input())
h=list(map(int,input().split()))

c=0
d=[]

if n==1:
    print('0')
    return

for i in range(n-1):
    if h[i]>=h[i+1]:
        c+=1
    else:
        d.append(c)
        c=0
    d.append(c)

print((max(d)))

