(a, b) = map(int, input().split())
print('IMPOSSIBLE' if a % 2 != b % 2 else (a + b) // 2)
