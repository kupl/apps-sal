b = [0] * 1001
x = int(input())
b[1] = 1
for i in range(2, 1000, 1):
    j = i * i
    while j < 1001:
        b[j] = 1
        j *= i
for i in range(x, 0, -1):
    if b[i] == 1:
        print(i)
        break
