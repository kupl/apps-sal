(a, b) = map(int, input().split())
print((-a ^ b) >> 1 & 1 ^ [b, 1][b & 1] ^ (a & 1) * a)
