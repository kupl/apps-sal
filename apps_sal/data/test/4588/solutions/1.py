(X, Y) = input().split()
temp = 'ABCDEF'
if temp.index(X) > temp.index(Y):
    print('>')
elif temp.index(X) == temp.index(Y):
    print('=')
else:
    print('<')
