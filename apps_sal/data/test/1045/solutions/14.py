cubes = int(input())

remove = 1
height = 0
add = 2
while(cubes > 0):
    cubes -= remove
    remove += add
    height += 1
    add += 1

if cubes == 0:
    print(height)
else:
    print(height - 1)
