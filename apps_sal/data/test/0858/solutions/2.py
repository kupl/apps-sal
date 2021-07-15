from math import log2, floor
N = int(input())
if N % 2 == 0:
    N //= 2
    ans = N - 2 ** floor(log2(N))
else:
    ans = (N+1) // 2 - 1
print(ans)
