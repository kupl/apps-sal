import math
(X, Y) = input().split()
X = ord(X)
Y = ord(Y)
if X == Y:
    print('=')
elif X > Y:
    print('>')
else:
    print('<')
