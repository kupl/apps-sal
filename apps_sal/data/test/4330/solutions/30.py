a,b=map(int,input().split())
if (b-a)/2%1==0:
    s=a+(b-a)//2
else:
    s="IMPOSSIBLE"
print(s)
