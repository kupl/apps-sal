s=input()

if(s[0]!='-'):
    print(s)

else:
    y=""
    n=len(s)
    for i in range(n):
        if(i==n-1):
            continue
        y+=s[i]
    z=""
    for i in range(n):
        if(i==n-2):
            continue
        z+=s[i]
    z=int(z)
    y=int(y)
    if(y>z):
        print(y)
    else:
        print(z)
        

