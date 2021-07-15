N, T = list(map(int,input().split()))
A = list(map(int,input().split()))

ans = 0 
for i in range(len(A)-1):
    ans += min(T,A[i+1]-A[i])

print(ans+T)
