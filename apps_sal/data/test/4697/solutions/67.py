n, m = list(map(int, input().split()))

if n >= m // 2:
    ans = m // 2
else:
    m -= n * 2
    ans = n + m // 4

print(ans)
