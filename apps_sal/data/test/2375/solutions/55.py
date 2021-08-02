x, y = list(map(int, input().split()))

print(("Alice" if abs(x - y) > 1 else "Brown"))
