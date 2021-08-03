a, b, c, d = map(int, input().split())
L = a + b
R = c + d
print("Left" if L > R else "Right" if R > L else "Balanced")
