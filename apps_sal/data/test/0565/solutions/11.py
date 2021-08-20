(y, b, r) = list(map(int, input().split()))
b_y = b - 1
r_y = r - 2
print((min(y, b_y, r_y) + 1) * 3)
