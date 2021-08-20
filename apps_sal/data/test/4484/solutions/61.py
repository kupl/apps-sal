import math
(N, M) = map(int, input().split())
mod = 10 ** 9 + 7
if abs(N - M) > 1:
    ans = 0
elif abs(N - M) == 1:
    ans = math.factorial(N) % mod * (math.factorial(M) % mod)
else:
    ans = math.factorial(N) % mod * (math.factorial(M) % mod) * 2
print(ans % mod)
