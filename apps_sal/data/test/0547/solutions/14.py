n,k=[int(a) for a in input().split()]
p=[]
for i in range(n):
    p.append(input())
real=input()
l=len(real)
cmin,cmax=0,0
for s in p:
    if len(s)<=l:
        cmax=cmax+1
        if len(s)<l:
            cmin=cmin+1

def calc(c):
    if c==0:
        return 0
    return c+5*(c//k)

print(calc(cmin)+1,calc(cmax-1)+1)

