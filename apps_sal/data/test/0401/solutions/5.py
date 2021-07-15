n,k=map(int,input().split(' '))
m=list(map(int,input().split(' ')))
m.sort()
h=list(map(int,input().split(' ')))
h.sort()
p=0
for i in m:
    if i in h:
        print(i)
        p=1
        break
if p==0:
    print(min(m[0]*10+h[0],h[0]*10+m[0]))
