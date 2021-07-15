import math
N = int(input())
ans = 1
q = [1 for i in range(N + 1)]
for i in range(2,N + 1):
    k = i
    for i2 in range(2,i + 1):
        while k % i2 == 0:
            k /= i2
            q[i2] += 1
            
for i in range(N + 1):
    ans *= q[i]
    ans %= 10 ** 9 + 7

print(ans)
