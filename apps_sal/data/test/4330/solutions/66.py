a, b = map(int, input().split())
print('IMPOSSIBLE' if (a ^ b) & 1 else (a + b) >> 1)
