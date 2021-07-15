o=input()
e=input()
O=len(o)
E=len(e)
a=[]
if O==E:
    for i in range(O):
        a.append(o[i]+e[i])
    b=''.join(a)
    print(b)
else:
    for i in range(E):
        a.append(o[i]+e[i])
    a.append(o[O-1])
    b=''.join(a)
    print(b)
