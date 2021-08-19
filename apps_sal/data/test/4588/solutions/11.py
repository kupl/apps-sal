lst = input().split()
X = lst[0]
Y = lst[1]
lst.sort()
if X == Y:
    print('=')
elif X == lst[0]:
    print('<')
else:
    print('>')
