def func(x, y):
    f1 = y * (y + 1) // 2
    f2 = x * (x + 1) // 2
    return (x + 1) * f1 + (y + 1) * f2


(m, b) = input().split()
m = int(m)
b = int(b)
y = b
maxi = 0
for i in range(0, m * b + 1, m):
    if func(i, y) > maxi:
        maxi = func(i, y)
    y -= 1
print(maxi)
