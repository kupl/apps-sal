import math
N = int(input())
L = list(map(int, input().split()))
ans = L[0]
for i in range(N - 1):
    ans = math.gcd(ans, L[i + 1])
print(ans)
