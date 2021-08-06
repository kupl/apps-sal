n = int(input())
b = [0] * n
c = [0] * n
array = []
for i in input().split():
    array.append(int(i))
    b[int(i) - 1] += 1
    c[int(i) - 1] = True
free = []
count = 0
for i in range(n):
    if b[i] == 0:
        free.append(i + 1)
    else:
        count += b[i] - 1
print(count)
z = 0
for i in range(n):
    if b[array[i] - 1] > 1:
        if array[i] > free[z]:
            b[array[i] - 1] -= 1
            array[i] = free[z]
            z += 1
        elif c[array[i] - 1] == False:
            b[array[i] - 1] -= 1
            array[i] = free[z]
            z += 1
        else:
            c[array[i] - 1] = False
for i in range(n):
    print(array[i], end=' ')
