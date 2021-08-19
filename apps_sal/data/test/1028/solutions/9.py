(a, b) = map(int, input().split())
x = a - b + 1
res1 = x * (x - 1) // 2
y = a // b
z = a % b
res2 = (b - z) * (y * (y - 1) // 2) + z * ((y + 1) * y // 2)
print(str(res2) + ' ' + str(res1))
