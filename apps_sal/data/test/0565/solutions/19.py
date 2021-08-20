(a, b, c) = [int(i) for i in input().split()]
print(min(a, b - 1, c - 2) * 3 + 3)
