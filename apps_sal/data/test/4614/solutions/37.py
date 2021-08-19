(x, y, z) = map(int, input().split())
print(z if x == y else y if x == z else x)
