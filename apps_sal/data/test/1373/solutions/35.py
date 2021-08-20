(n, k) = map(int, input().split())
ans = 0
for i in range(k, n + 2):
    ans += (n + n - i + 1) * i // 2 - (i - 1) * i // 2 + 1
print(ans % (10 ** 9 + 7))
