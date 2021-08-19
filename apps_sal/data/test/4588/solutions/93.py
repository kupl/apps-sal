import sys
(X, Y) = sys.stdin.readline().strip().split()
if X == Y:
    print('=')
elif X < Y:
    print('<')
else:
    print('>')
