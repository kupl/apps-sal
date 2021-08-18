a = input()
b = input()
if len(a) > len(b):
    b = '0' * (len(a) - len(b)) + b
else:
    a = '0' * (len(b) - len(a)) + a
for i in range(0, len(a)):
    if(a[i] > b[i]):
        print('>')
        return
    elif(b[i] > a[i]):
        print('<')
        return
print('=')
