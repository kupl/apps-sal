a=input()
b=input()
c=input()
i=0
j=0
k=0
t='a'
while 1:
    if t=='a':
        if i==len(a):
            print('A')
            break
        t=a[i]
        i+=1
    elif t=='b':
        if j==len(b):
            print('B')
            break
        t=b[j]
        j+=1
    elif t=='c':
        if k==len(c):
            print('C')
            break
        t=c[k]
        k+=1

