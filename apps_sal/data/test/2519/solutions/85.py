N,K = map(int,input().split())
p = list(map(int,input().split()))
ans = sum(p[0:K])
s = ans
for i in range(1,N-K+1):
    s += p[i+K-1]-p[i-1]
    ans = max(ans,s)
print((K+ans)/2)
