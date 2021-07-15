N,M=map(int,input().split())
*X,=sorted(map(int,input().split()))
print(sum(sorted([abs(X[i+1]-X[i]) for i in range(M-1)],reverse=True)[N-1:]))
