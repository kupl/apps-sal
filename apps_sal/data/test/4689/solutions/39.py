K,N = map(int,input().split())
A = [int(i) for i in input().split()]
L = []
ans = 0
for i in range(N):
    if(i == N-1):
        L.append(K-A[N-1]+A[0])
        break
    L.append(A[i+1]-A[i])
for i in range(N):
    ans += L[i]
ans -= max(L)
print(ans)
