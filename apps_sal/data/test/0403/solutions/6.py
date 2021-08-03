M = input().split()
n = int(M[0])
x = int(M[1])
y = int(M[2])
M = input().split()
for i in range(0, n):
    M[i] = int(M[i])
M.sort()

c = 0
for i in range(0, n):
    if M[i] > 0:
        dy = M[i] % 2
        dx = (M[i] - dy) // 2
        x = x - dx
        y = y - dy
        if x < 0:
            y += x * 2
            x = 0
            if y < 0:
                break
        if y < 0:
            x += y
            y = 0
            if x < 0:
                break
        if (x >= 0) and (y >= 0):
            c += 1
    M[i] = 0
    if (x == 0) and (y == 0):
        break


ndone = n
for i in range(0, n):
    if M[i] > 0:
        ndone += -1
print(ndone)
