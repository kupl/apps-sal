(n, m) = list(map(int, input().split()))
(a, b) = list(map(int, input().split()))
ans = m * (a / b)
for i in range(1, n):
    (a, b) = list(map(int, input().split()))
    ans = min(ans, m * (a / b))
print('%.7f' % ans)
