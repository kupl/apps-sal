a = int(input(''))
b = bin(a)[2:]
b = '0' * (6 - len(b)) + b
ans = b[0] + b[5] + b[3] + b[2] + b[4] + b[1]
print(int('0b' + ans, 2))
