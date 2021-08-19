(n, m, k) = map(int, input().split())
st = [list(map(int, input().split())) for _ in range(2 * k)]
print(n * m + n + m - 3)
ans = ''
ans += 'U' * (n - 1)
ans += 'L' * (m - 1)
ans += 'D' * (n - 1)
cur = 1
while cur < m:
    ans += 'R'
    if cur % 2 == 1:
        ans += 'U' * (n - 1)
    else:
        ans += 'D' * (n - 1)
    cur += 1
print(ans)
