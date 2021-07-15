a=int(input())
b=[]
b.append(a)
while True:
    if a%2==0:
        a=a/2
        if a in b:
            print(len(b)+1)
            break
        else:
            b.append(a)
    elif a%2!=0:
        a=3*a+1
        if a in b:
            print(len(b)+1)
            break
        else:
            b.append(a)
