(n, k) = map(int, input().split())
i = 1
cnt = 0
while i <= n:
    i *= k
    cnt += 1
print(cnt)
