import math
N = int(input())
ans = 1
for i in range(N):
    a = int(input())
    ans = ans * a // math.gcd(ans, a)
print(ans)
