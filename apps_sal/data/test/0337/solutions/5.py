w,h=map(int,input().split())
d1,u1=map(int,input().split())
d2,u2=map(int,input().split())
for x in range(h,-1,-1):
    w+=x
    if(x==u1):
        w=max(0,w-d1)
    if(x==u2):
        w=max(0,w-d2)
print(w)
