import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
N -= K
ans = 1
if N <= 0:
    print(ans)
    return
ans += math.ceil(N / (K - 1))
print(ans)
