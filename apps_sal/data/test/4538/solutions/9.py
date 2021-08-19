import math
(n, d) = list(map(int, input().split()))
ans = 0
for i in range(n):
    (x, y) = list(map(int, input().split()))
    if d >= math.sqrt(x ** 2 + y ** 2):
        ans += 1
print(ans)
