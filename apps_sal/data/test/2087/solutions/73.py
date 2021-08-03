m = 998244353
a, b, c = map(int, input().split())

a %= m
b %= m
c %= m
ans = a * (a + 1) // 2 % m
ans *= b * (b + 1) // 2 % m
ans *= c * (c + 1) // 2 % m
print(ans % m)
