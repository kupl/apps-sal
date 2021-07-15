N,M=map(int,input().split())
A=list(map(int,input().split()))
A_sum=sum(A)
if A_sum>N:
    print("-1")
else:
    print(N-A_sum)
