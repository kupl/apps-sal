x = int(input())
x = bin(x)[2:]
x = list(x)
x = ['0'] * (6 - len(x)) + x
temp = x[5]
x[5] = x[1]
x[1] = temp
temp = x[2]
x[2] = x[3]
x[3] = temp
x = ''.join(x)
print(int(x, 2))
