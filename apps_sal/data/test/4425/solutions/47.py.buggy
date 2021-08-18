import math
N, K = map(int, input().split())
if K == 1:
    print(1)
    return

ans = 0

for i in range(1, N + 1):
    if i >= K:
        ans += (1 / N)
    else:
        temp = math.log(K / i, 2)
        nu = pow(2, math.ceil(temp))
        ans += (1 / (nu * N))
print(ans)
