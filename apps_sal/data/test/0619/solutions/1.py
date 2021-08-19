(x, y, z) = list(map(int, input().split()))
ans1 = x // z + y // z
x = x % z
y = y % z
if x + y >= z:
    print(ans1 + 1, min(z - x, z - y))
else:
    print(ans1, 0)
