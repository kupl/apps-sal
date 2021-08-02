a, b, c, d = map(int, input().split())
print("Left" if c + d < a + b else "Right" if c + d > a + b else "Balanced")
