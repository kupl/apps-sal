
rStr = input()

H = int(rStr.split(' ')[0])
A = int(rStr.split(' ')[1])

count = 0

while (0 < H):
    H = H - A
    count = count + 1

print(count)
