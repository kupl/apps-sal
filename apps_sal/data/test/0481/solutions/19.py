(n, x) = map(int, input().split())
cnt = 0
for i in range(1, n + 1):
    if x // i == x / i and x // i <= n:
        cnt += 1
print(cnt)
