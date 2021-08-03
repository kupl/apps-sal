x, y, z = list(map(int, input().split()))
tmp = y
y = x
x = tmp

tmp2 = z
z = x
x = tmp2
print(("{} {} {}".format(x, y, z)))
