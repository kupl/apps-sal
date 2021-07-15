#ABC167
A,B,C,K=map(int,input().split())
#----------以上入力----------
if A > K:
    print(K)
elif  A+B >= K:
    print(A)
else:
    print(A-(K-A-B))
