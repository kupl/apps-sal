import math

n, k = map(int, input().split())
ans = 0
x = [max(0, math.ceil(math.log2(k / i))) for i in range(1, n + 1)]
for i in x:
    ans += ((2 ** i) * n) ** -1 
print(ans)
