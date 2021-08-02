n, a, b = list(map(int, input().split(" ")))
ans = 0
for i in range(1, n):
    m = min(a // i, b // (n - i))
    if m > ans:
        ans = m
print(ans)
