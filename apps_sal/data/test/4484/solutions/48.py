N,M =map(int,input().split())
a = abs(N-M)
mod = 10**9 + 7
n = 1
for i in range(N):
    n *= N-i
    n %= mod
m = 1
for i in range(M):
    m *= M-i
    m %= mod
if a > 1:
    print(0)
elif a == 1:
    print(n * m % mod)
else:
    print(n*m*2%mod)
