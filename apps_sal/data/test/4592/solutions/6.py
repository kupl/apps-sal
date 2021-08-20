import math
N = int(input())
m = math.factorial(N)
A = 1000 * [1]
ans = 1
for n in range(2, 1001):
    while m % n == 0:
        m //= n
        A[n] += 1
for a in A:
    ans *= a
print(ans % (10 ** 9 + 7))
