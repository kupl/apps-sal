import math
n = int(input())
z = math.floor(math.sqrt(n))
ans = 10 ** 12
for i in range(1,z+1):
    if n % i == 0:
        m = n // i
        ans = min(ans,m+i-2)
print(ans)
