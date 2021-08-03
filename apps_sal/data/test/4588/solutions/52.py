X, Y = input().split()
alphabet = ['A', 'B', 'C', 'D', 'E', 'F']
x_i = 0
y_i = 0
for i in range(6):
    if alphabet[i] == X:
        x_i = i
    if alphabet[i] == Y:
        y_i = i
if x_i < y_i:
    print('<')
elif x_i > y_i:
    print('>')
else:
    print('=')
