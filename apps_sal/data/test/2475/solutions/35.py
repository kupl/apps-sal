N = int(input())
S = list(map(int,input().split()))

ans = 0
for C in range(1,N):
    dp = 0
    for k in range((N-1)//C):
        if (2*k-1)*C == N-1 or 2*k*C == N-1:
            break
        dp += S[N-1-C*k]+S[C*k]
        ans = max(ans,dp)

print(ans)
