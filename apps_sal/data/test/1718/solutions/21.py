N,K = map(int,input().split())
A = list(map(int,input().split()))
n = N-1
k = K-1
ans = (n+k-1)//k
print(ans)
