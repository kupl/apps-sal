a = input()
b = input()
if len(a) > len(b):
    b = '0' * (len(a) - len(b)) + b
else:
    a = '0' * (len(b) - len(a)) + a
if(a > b):
    print('>')
elif(b > a):
    print('<')
else:
    print('=')
