x, y, z = map(int, input().split())

num = x // (y + z)
if x >= num * y + (num * z + z):
    print(num)
else:
    print(num - 1)
