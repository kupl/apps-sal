with open(0) as f:
    N, M = map(int, f.read().split())
mod = 1000000007

def factorial(n):
    res = 1
    for i in range(1,n+1):
        res = res * i %mod
    return res

if abs(N-M) > 1:
    ans = 0
elif N == M:
    ans = 2*factorial(M)**2 %mod 
else:
    N, M = max(N, M), min(N, M)
    ans = N * factorial(M)**2 %mod
print(ans)
