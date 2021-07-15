N = int(input())

count = 0
y = 0
x = 0
while count != N:
    count += 1
    if count % 15 == 0:
        y += 200
    x += 800

print((x - y))

