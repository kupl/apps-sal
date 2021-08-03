3

r, h = tuple(map(int, input().split()))
ans = (2 * h + r) // (2 * r)
print(2 * ans + (3 * r**2 <= 4 * (h + r - ans * r)**2))
