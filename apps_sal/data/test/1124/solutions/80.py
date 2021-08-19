from math import gcd
n = int(input())
A = list(map(int, input().split()))
A = list(set(A))
n = len(A)
ans = A[0]
for i in range(n):
    ans = gcd(ans, A[i])
print(ans)
