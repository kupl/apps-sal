str = input()
inpt = ''
n = int(str)
x = 0
for i in range(n):
    inpt = input()
    if inpt[0:2] == '++' or inpt[1:3] == '++':
        x += 1
    elif inpt[0:2] == '--' or inpt[1:3] == '--':
        x -= 1
print(x)
