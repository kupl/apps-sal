from math import floor
N,K = map(int,input().split())
ans = 0
for b in range(K+1, N+1):
    p,r = N//b,N%b
    ans += p*max(0,b-K)+max(0,r-K+1)
print(ans if K!=0 else ans-max(0,b-K))
