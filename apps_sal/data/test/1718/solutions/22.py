N,K=list(map(int,input().split()))
a=list(map(int,input().split()))

tmp=(N-1)//(K-1)
if tmp*(K-1)==N-1:
    print(tmp)
else:
    print((tmp+1))


