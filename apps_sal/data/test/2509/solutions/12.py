N,K = map(int,input().split())
ans = 0
if K == 0:
    print(N**2)
    return
for b in range(K+1,N+1):
    per = N//b
    rem = N%b
    if rem >= K:
        ans += (per+1)*(rem-K+1) + per * (b-1-rem)
    else:
        ans += per * (b-K)
print(ans)
