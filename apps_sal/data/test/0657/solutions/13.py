A, B = list(map(int, input().split()))
x, y, z = list(map(int, input().split()))

a, b = 0, 0

a += 2 * x
a += y
b += y
b += 3 * z

print(max(0, a - A) + max(0, b - B))

