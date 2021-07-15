n=int(input())
a=input()
a=a.replace(' ','')
a=a+'00'
c=2
h=0
for i in a:
    if i=='0':
        c+=1
    else:
        if c==1:
            h+=2
        else:
            h+=1
        c=0
print(h)
