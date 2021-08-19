(n, m) = map(int, input().split())
ans = 1
for i in range(1, int(m ** 0.5) + 1):
    if m % i == 0:
        if i >= n:
            ans = max(ans, m // i)
        elif m // i >= n:
            ans = max(ans, i)
print(ans)
