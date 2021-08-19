# 21 C - Dice and Coin
import math
N, K = map(int, input().split())

ans = 0
for i in range(1, N + 1):
    if K // i != 0:
        a = math.log2(K / i)
        if a.is_integer():
            x = int(a)
        else:
            x = int(a) + 1
        ans += (1 / N) * (1 / 2)**x
    else:
        ans += (1 / N)
print(ans)
