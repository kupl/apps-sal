A, B = map(int, input().split())
x, y, z = map(int, input().split())
nem = x * 2 + y
nes = z * 3 + y
print(max(nem - A, 0) + max(nes - B, 0))
