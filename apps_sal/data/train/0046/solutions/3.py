
t=int(input())
for you in range(t):
    s=input()
    n=len(s)
    numofr=0
    numofs=0
    numofp=0
    for i in s:
        if(i=='R'):
            numofr+=1
        elif(i=='S'):
            numofs+=1
        else:
            numofp+=1
    z=max(numofr,numofp,numofs)
    if(z==numofr):
        print('P'*n)
    elif(z==numofs):
        print('R'*n)
    else:
        print('S'*n)
