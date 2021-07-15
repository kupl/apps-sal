A, B, C = map(int,input().split())
M = 998244353

x = (1 + A) * A // 2
y = (1 + B) * B // 2
z = (1 + C) * C // 2
x %= M
y %= M
z %= M
ans = (x * y * z) % M
print(ans)
