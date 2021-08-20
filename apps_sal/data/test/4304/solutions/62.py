(a, b) = map(int, input().split())
c = b - a
c = (1 + c) * c // 2
print(c - b)
