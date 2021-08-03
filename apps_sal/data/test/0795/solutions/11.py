from math import sqrt as sq
from math import gcd
ans = 0
n = int(input())
N = n * n
for i in range(2, int(sq(n + 1)) + 2):
    for j in range(1 + i & 1, i, 2):
        if i * i + j * j > N:
            break
        if gcd(i, j) == 1:
            ans += int(n / (i * i + j * j))
print(ans)
