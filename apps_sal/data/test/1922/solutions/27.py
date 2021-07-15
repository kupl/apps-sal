
N, M = list(map(int,input().split()))

if(N*M==2):
    print((0))
    return
if(N*M==1):
    print((1))
    return
if(N==1):
    print((M-2))
    return
if(M==1):
    print((N-2))
    return
print(((N-2)*(M-2)))


