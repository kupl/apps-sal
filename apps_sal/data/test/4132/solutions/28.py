import math
n = int(input())
*A, = list(map(int, input().split()))
ans = A[0]
for a in A:
    ans = math.gcd(ans, a)
print(ans)
