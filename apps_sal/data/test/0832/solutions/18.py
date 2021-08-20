n = int(input())
tshirt = []
for i in range(n):
    x = list(map(int, input().split()))
    tshirt.append(x)
count = 0
for y in range(n):
    for z in range(n):
        if tshirt[y][0] == tshirt[z][1]:
            count += 1
print(count)
