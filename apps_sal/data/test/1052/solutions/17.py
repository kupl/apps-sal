def factorial(k):
    ans = 1
    for i in range(1, k+1):
        ans *= i
    return ans

n, k = list(map(int, input().split()))
ans = 0;
def A(n, m):
    ans = 1
    for x in range(m + 1, n+1):
        ans *= x
    return ans

for i in range(2, k+1):
    si = 0
    for j in range(2, i+1):
        coeff = -1 if j%2 else 1 
        si += coeff/factorial(j)
    ans += A(n, n-i)*si
    

print(int(ans + 1.5))

