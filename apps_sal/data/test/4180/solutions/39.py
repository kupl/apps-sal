n = int(input())
roop = True
x = 0
while roop:
    x += 1
    if 1000 * x >= n:
        roop = False
print((1000 * x) - n)
