a, b, c = map(int, input().split())

ans = a * (a + 1) * b * (b + 1) * c * (c + 1) // 8

print(int(ans % 998244353))
