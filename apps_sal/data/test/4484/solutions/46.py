def factorial(a):
    result = 1
    for i in range(1,a+1):
        result *= i
        result %= 1000000007
    return result
N, M = map(int, input().split())
if N == M:
    ans = 2*(factorial(N)**2) %1000000007
elif abs(N-M) == 1:
    ans = max(N,M)*(factorial(min(N,M))**2) %1000000007
else:
    ans =0
print(ans)
