import sys
input=sys.stdin.readline
n,a,b=map(int,input().split())
h=[]
for i in range(n):
    h.append(int(input()))

def enough(t):
    tmp=0
    for i in range(n):
        if h[i]>b*t:
            tmp+=(h[i]-b*t)//(a-b)+(1 if (h[i]-b*t)%(a-b)>0 else 0)
    return True if tmp<=t else False

ok=max(h)
ng=0
mid=(ok-ng)//2
while abs(ok-ng)>1:
    if enough(mid):
        ok=mid
    else:
        ng=mid
    mid=(ok+ng)//2
print(ok)
