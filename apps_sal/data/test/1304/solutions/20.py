z=[]
for i in range(11):
    if (i!=3 and i!=7):
        a,b,c=input().split()
        l=a+b+c
        z.append(l)
    else:
        p=input()

y,x=map(int,input().split())
y=(y-1)%3
x=(x-1)%3
flag=0
for i in range(y*3,y*3+3):
    for j in range(x*3,x*3+3):
        if z[i][j]=='.':
            flag=1
if flag==1:
    for i in range(9):
        for j in range(9):
            if (i>=(y*3)) and (i<(y*3+3)) and (j>=(x*3)) and (j<(x*3+3)):
                if z[i][j]=='.':
                    print('!',end='')
                else:
                    print(z[i][j],end='')
            else:
                print(z[i][j],end='')
            if ((j+1)%3==0) and j!=8:
                print(' ',end='')
            if (j==8):
                print()
        if ((i+1)%3==0) and i!=8:
            print()
else:
    for i in range(9):
        for j in range(9):
            if z[i][j]=='.':
                print('!',end='')
            else:
                print(z[i][j],end='')
            if ((j+1)%3==0) and j!=8:
                print(' ',end='')
            if (j==8):
                print()
        if ((i+1)%3==0) and i!=8:
            print()
        

