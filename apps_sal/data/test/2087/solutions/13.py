(a, b, c) = list(map(int, input().split()))
sum = 0
sum = a * b * c * (a + 1) * (b + 1) * (c + 1) // 8
print(int(sum % 998244353))
