n, m = list(map(int, input().split()))

ans = 0
while True:
    if n == m == 1:
        break
    if n == 0 or m == 0:
        break
    if n >= m:
        n -= 2
        m -= 1
    else:
        n -= 1
        m -= 2
    ans += 1
print(ans)
