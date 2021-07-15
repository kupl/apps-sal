t=int(input())
l=list(map(int,input().split()))
if len(l)==1:
    print("-1")
elif len(l)==2 and len(set(l))==1:
    print("-1")
else:
    print(1)
    print(l.index(min(l))+1)

