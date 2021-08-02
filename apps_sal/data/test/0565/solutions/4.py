y, b, r = list(map(int, input().split()))
print(min(y, b - 1, r - 2) * 3 + 3)
