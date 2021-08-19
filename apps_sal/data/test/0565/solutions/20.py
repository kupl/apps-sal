(y, b, r) = list(map(int, input().split()))
x = min(y, b - 1, r - 2)
print(x * 3 + 3)
