import collections
import math

def is_prime(x): 
    for i in range(2, math.ceil(math.sqrt(x))):
        if x % i == 0:
            return False
    return True

n, k = map(int, input().split())
T = [[0] * n for _ in range(n)]
ans = 0
s = n * n
for i in range(n):
    for j in range(n - k + 1):
        T[i][n - j - 1] = s
        s -= 1
a = 1
for i in range(n):
    for j in range(k - 1):
        T[i][j] = a
        a += 1
for i in range(n):
    ans += T[i][k - 1]
print(ans)
for i in range(n):
    print(' '.join(map(str, T[i])))
