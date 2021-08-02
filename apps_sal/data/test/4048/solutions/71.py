import math
n = int(input())
root_n = math.floor(math.sqrt(n))
ans = 0
for i in range(1, root_n + 1):
    if n % i == 0:
        ans = i
print(int(ans + n / ans - 2))
