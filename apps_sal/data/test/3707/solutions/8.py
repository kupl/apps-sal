(n, t, k, d) = map(int, input().split())
ans = 0
i = 0
while ans < n:
    i += 1
    if i % t == 0:
        ans += k
    if i - d > 0 and (i - d) % t == 0 and (ans < n):
        print('YES')
        break
else:
    print('NO')
