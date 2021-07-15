N,K = list(map(int,input().split()))
ans = 0
for i in range(K,N+2):
    ans += (((2*N-i+1)*i) // 2 - ((i-1)*i)//2)+1
    ans = ans % (10**9+7)
print(ans)

