n,k,d=list(map(int,input().split()))
if n>k**d:print((-1));return
K=1
for j in range(d):
    print(" ".join([str(i//K%k +1) for i in range(n)]))
    K*=k

