res = []
for digit in range(1, 16):
    if digit <= 3:
        for i in range(2, 11):
            res.append(10 ** (digit - 1) * i - 1)
    elif 4 <= digit <= 12:
        for i in range(11, (digit - 2) * 10):
            res.append(i * 10 ** (digit - 2) - 1)
        for i in range(digit - 2, 11):
            res.append(i * 10 ** (digit - 1) - 1)
    elif digit == 15:
        for i in range(101, 110):
            res.append(i * 10 ** (digit - 3) - 1)
        for i in range(11, 101):
            res.append(i * 10 ** (digit - 2) - 1)
    else:
        for i in range(11, 101):
            res.append(i * 10 ** (digit - 2) - 1)
for i in range(int(input())):
    print(res[i])
