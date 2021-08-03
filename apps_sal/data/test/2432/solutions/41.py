n = int(input())
b = f'{n:b}'

while len(b) < 6:
    b = "0" + b

s = b[0] + b[5] + b[3] + b[2] + b[4] + b[1]

print(int(s, 2))
