from math import sqrt
(r, d) = map(int, input().split())
n = int(input())
ans = 0
for i in range(n):
    (x, y, c) = map(int, input().split())
    if max(sqrt(x ** 2 + y ** 2) - c, 0) >= r - d and sqrt(x ** 2 + y ** 2) + c <= r:
        ans += 1
print(ans)
