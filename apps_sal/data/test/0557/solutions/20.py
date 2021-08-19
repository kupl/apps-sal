(n, m) = map(int, input().split())
maxRight = 0
for _ in range(n):
    (a, b) = map(int, input().split())
    if a > maxRight:
        break
    maxRight = max(maxRight, b)
if maxRight >= m:
    print('YES')
else:
    print('NO')
