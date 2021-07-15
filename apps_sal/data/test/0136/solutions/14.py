a=input().lstrip('0')
b=input().lstrip('0')
dlinaA=len(a)
dlinaB=len(b)
if dlinaA==0:
    a='0'
if dlinaB==0:
    b='0'
if dlinaA==0 and dlinaB==0:
    print('=')
if dlinaA>dlinaB:
    print('>')
elif dlinaA<dlinaB:
    print('<')
else:
    for i in range(dlinaA):
        if int(a[i])>int(b[i]):
            print('>')
            break
        elif int(a[i])<int(b[i]):
            print('<')
            break
        elif i==dlinaA-1:
            print('=')
            break


