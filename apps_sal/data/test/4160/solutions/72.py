X = int(input())
Y, M = 0, 100
while M < X:
    M += M // 100
    Y += 1
print(Y)
