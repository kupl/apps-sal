#Presents
#Codeforces 256

a,b,c=input().split()
d,e,f=input().split()

cups=int(a)+int(b)+int(c)

medals=int(d)+int(e)+int(f)

shelves=int(input())

while shelves>0:
    if cups>0:
        cups=cups-5
    elif cups<=0 and medals>0:
        medals=medals-10
    shelves=shelves-1

if cups<=0 and medals<=0:
    print("YES")

else:
    print("NO")

