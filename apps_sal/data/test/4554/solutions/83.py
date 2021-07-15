w, a, b = map(int, input().split())

print(max(a, b) - min(a, b) - w) if abs(a -  b) > w else print(0)
