t=int(input())
for x in range(t):
    l=input()
    flag=3
    if(l.startswith('miao.')==True):
        flag=2
    if(l.endswith('lala.')==True):
        flag=1
    if(l.startswith('miao.')==True) and (l.endswith('lala.')==True):
        flag=3
    if(flag==3):
        print("OMG>.< I don't know!")
    if(flag==2):
        print("Rainbow's")
    if(flag==1):
        print("Freda's")

