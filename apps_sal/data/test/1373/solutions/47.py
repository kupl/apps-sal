(n, k) = map(int, input().split())
ans = 1
y = sum(list(range(n - k + 2, n + 1)))
j = n - k + 1
for i in range(k, n + 1):
    x = (1 + (i - 1)) * (i - 1) // 2
    y += j
    j -= 1
    ans += y - x + 1
    ans %= 10 ** 9 + 7
print(ans)
