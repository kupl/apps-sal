import math
(N, M) = map(int, input().split())
t = 10 ** 9 + 7
n = math.factorial(N) % t
m = math.factorial(M) % t
if 2 <= abs(N - M):
    print(0)
elif abs(N - M) == 1:
    print(n * m % t)
else:
    print(n * m * 2 % t)
