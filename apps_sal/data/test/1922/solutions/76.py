d=list(map(int,input().split()))
N=min(d)
M=max(d)
if N>=2:
    print((N-2)*(M-2))
else:
    if M==1:
        print(1)
    else:
        print(M-2)
