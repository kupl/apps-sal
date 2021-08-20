(x, y) = input().split()
if x == y:
    print('=')
elif ord(x) > ord(y):
    print('>')
else:
    print('<')
