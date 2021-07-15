a = input()
b = input()
if len(a)>len(b):
    gap = len(a)-len(b)
    new = ''
    for _ in range(gap):
        new+='0'
    b = new + b
elif len(b)>len(a):
    gap = len(b) - len(a)
    new = ''
    for _ in range(gap):
        new+='0'
    a = new + a
for i in range(0,len(a)):
    if(a[i]>b[i]):
        print('>')
        return
    elif(b[i]>a[i]):
        print('<')
        return
print('=') 
