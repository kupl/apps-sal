x = bin(int(input()))
t = 0
nrr = []
while True:
    for i in range(2, len(x)):
        if x[i] == '0':
            break
    else:
        break
    t += 1
    if t % 2:
        for i in range(2, len(x)):
            if x[i] == '0':
                n = len(x) - i
                x = bin(int(x, 2) ^ 2 ** n - 1)
                nrr.append(n)
                break
    else:
        x = bin(int(x, 2) + 1)
print(t)
for n in nrr:
    print(n, end=' ')
