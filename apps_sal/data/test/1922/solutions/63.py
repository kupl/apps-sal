N,M=map(int,input().split())

if N==2 or M==2 :
    B=0
elif N==1 or M==1 :
    if N==M :
        B=1
    elif N<M:
        B=M-2
    else:
        B=N-2
else:
    B=N*M-M*2-N*2+4
    
print(B)
