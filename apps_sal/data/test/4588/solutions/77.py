X, Y = input().split()
x_i = ord(X)
y_i = ord(Y)
if x_i < y_i:
    print('<')
elif x_i > y_i:
    print('>')
else:
    print('=')
