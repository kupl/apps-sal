N,K=map(int,input().split())
hi=list(map(int,input().split()))
HI=[i for i in hi if i>=K]
print(len(HI))
