a, b = map(int, input().split())
a -= 1
print(a >> 1 & 1 ^ b >> 1 & 1 ^ [b, 1][b & 1] ^ [a, 1][a & 1])
