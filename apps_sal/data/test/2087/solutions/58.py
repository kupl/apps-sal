(a, b, c) = list(map(int, input().split()))
a = a * (a + 1) // 2 % 998244353
b = b * (b + 1) // 2 % 998244353
c = c * (c + 1) // 2 % 998244353
print(a * b * c % 998244353)
