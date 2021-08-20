(n, m) = list(map(int, input().split()))
cnt = 0
while min(n, m) >= 1 and max(n, m) >= 2:
    (n, m) = (min(n, m), max(n, m))
    n -= 1
    m -= 2
    cnt += 1
print(cnt)
