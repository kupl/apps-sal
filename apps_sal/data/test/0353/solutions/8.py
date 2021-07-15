n=int(input())
l=list(map(int,input().split()))
if n==1:
    if l[0]==0: print("UP")
    elif l[0]==15: print("DOWN")
    else: print(-1)
elif (l[-1]==0 or l[-2]<l[-1]) and l[-1]!=15: print("UP")
else: print("DOWN")
