(a, b) = map(int, input().split())
ri = b - a
print(ri * (ri + 1) // 2 - b)
