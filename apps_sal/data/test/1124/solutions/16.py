import math
n = int(input())
(ans, *A) = map(int, input().split())
for a in A:
    ans = math.gcd(a, ans)
print(ans)
