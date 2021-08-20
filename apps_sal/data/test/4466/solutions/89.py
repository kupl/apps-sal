(x, y, z) = map(int, input().split())
x -= z
count = 0
while x >= y + z:
    x -= y + z
    count += 1
print(count)
