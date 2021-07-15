N=int(input());A=list(map(int,input().split()));j=1;fg=0
if N==1:
    if A[0]==1:print(0)
    else: print(-1)
else:
    for i in A:
        if i==j:j+=1
        else:fg+=1
    if j>1:print(fg)
    else: print(-1)
