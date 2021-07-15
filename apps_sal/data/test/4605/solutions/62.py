n, a, b = list(map(int, input().split()))

ans = 0
for x in range(1, n + 1):
    c = sum(map(int, str(x)))
    if a <= c <= b:
        ans += x
print(ans)

