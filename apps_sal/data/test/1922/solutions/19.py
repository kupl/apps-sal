(n, m) = map(int, input().split())
ans = 0
if n == 1 or m == 1:
    if n == 1 and m == 1:
        ans = 1
    else:
        ans = abs(n - m) - 1
else:
    ans = n * m - (2 * n + 2 * m) + 4
print(ans)
