def summaX(x):
    k=0
    for el in x:
        k+=int(el)
    return k
n=input();N=[];Z=[]
for el in n:
    N.append(el)
z=summaX(N)
Z=N.copy()
for i in range(1,len(N)):
    if int(N[i])!=9:
        N[i-1]=int(N[i-1])-1
        for j in range(i,len(n)):
            N[j]=9
if z>=summaX(N):
    for el in Z:
        print(el,end='')
else:
    if N[0]==0:
        N.pop(0)
    for el in N:
        print(el,end='')

