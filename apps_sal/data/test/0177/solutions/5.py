n=int(input())
x=1
while n!=0:
    for i in range(len(str(x))):
        if n!=0:
            s=str(x)[i]
            n-=1
    x+=1
print(s)
    

