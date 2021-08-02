a, b, c = map(int, input().split())

sum = (a * (a + 1)) // 2
sum *= (b * (b + 1)) // 2
sum *= (c * (c + 1)) // 2

print(sum % 998244353)
