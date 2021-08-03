a, b = map(int, input().split())
print(['IMPOSSIBLE', a + (b - a) // 2][(b - a) % 2 == 0])
