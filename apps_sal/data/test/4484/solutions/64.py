import math
(N, M) = map(int, input().split())
p = 10 ** 9 + 7
dog = math.factorial(N)
mon = math.factorial(M)
if N == M:
    ans = dog * mon * 2 % p
elif abs(N - M) == 1:
    ans = dog * mon % p
else:
    ans = 0
print(ans)
