(y, b, r) = list(map(int, input().split()))
k = min(y, b - 1, r - 2)
print(k * 3 + 3)
