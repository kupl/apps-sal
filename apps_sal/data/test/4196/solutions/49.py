import math
N = int(input())
List = list(map(int, input().split()))
L = [0] * N
R = [0] * N
for i in range(1, N):
    L[i] = math.gcd(L[i - 1], List[i - 1])
    R[-i - 1] = math.gcd(R[-i], List[-i])
ans = 0
for i in range(N):
    ans = max(ans, math.gcd(L[i], R[i]))
print(ans)
