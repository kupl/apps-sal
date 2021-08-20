import math
(A, B) = [int(_) for _ in input().split()]
N = math.gcd(A, B)
ans = 1
for i in range(2, int(math.sqrt(N) + 1) + 1):
    if N % i == 0:
        ans += 1
        while N % i == 0:
            N //= i
if N > 1:
    ans += 1
print(ans)
