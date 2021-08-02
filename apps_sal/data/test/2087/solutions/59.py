a, b, c, = list(map(int, input().split()))

ans = a * (a + 1) * b * (b + 1) * c * (c + 1) // 8
ans %= 998244353
print(ans)
