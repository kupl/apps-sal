(a, b, c) = list(map(int, input().split()))
result = int(a * (a + 1) // 2 * (b * (b + 1)) // 2 * (c * (c + 1)) // 2 % 998244353)
print(result)
