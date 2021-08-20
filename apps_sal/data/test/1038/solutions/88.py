(a, b) = map(int, input().split())
(c, d) = map(lambda x: x // 2 % 2 ^ 1 if x % 2 else x ^ x // 2 % 2, [a - 1, b])
print(c ^ d)
