import math
(n, d) = map(int, input().split())
x = [list(map(int, input().split())) for i in range(n)]
ans = 0
for (i, j) in x:
    if math.sqrt(i * i + j * j) <= d:
        ans += 1
print(ans)
