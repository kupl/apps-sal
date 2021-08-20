from math import sqrt
(n, m) = list(map(int, input().split()))
ans = 1
for i in range(1, int(sqrt(m) + 2)):
    if m % i == 0:
        if i <= m / n:
            ans = max(ans, i)
        if m // i <= m / n:
            ans = max(ans, m // i)
print(ans)
