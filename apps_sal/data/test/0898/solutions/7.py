from collections import defaultdict

n, m = list(map(int, input().split()))

ans = 0
i = 1
while i * i <= m:
    if m % i == 0:
        a, b = i, m // i
        if b >= n:
            ans = max(ans, a)
        if a >= n:
            ans = max(ans, b)
    i += 1
print(ans)
