(a, b) = map(int, input().split())
print(-(a ^ b) >> 1 & 1 ^ ~b % 2 * b ^ a % 2 * a)
