import math
n, m = list(map(int, input().split()))
num = int(math.sqrt(m))
ans = 1
for i in range(1, num + 2):
    if m % i == 0 and i >= n:
        ans = max(ans, m // i)
        break
    if m % i == 0 and m // i >= n:
        ans = max(ans, i)
print(ans)
