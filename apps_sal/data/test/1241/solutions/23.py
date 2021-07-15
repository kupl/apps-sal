from sys import stdin, stdout
L=list(map(int,stdin.readline().split()))
n=L[0]
k=L[1]
#a=list(map(int,stdin.readline().split()))
a=[int(c) for c in stdin.readline().split()]

nbr0=0
posi=0
taillemax=0
p=0
for i in range(len(a)):
    nbr0+=(a[i]==0)
    if nbr0>k:
        if (i-posi)>taillemax:
            
            p=posi
            taillemax=i-posi
           
        j=posi
        while 1:
            if a[j]==0:
                posi=j+1
                break
            j=j+1
        nbr0-=1
       
if i==(n-1) and (i-posi+1)>taillemax:
    p=posi
    taillemax=i-posi+1
    #print(p,posi)
    
print(taillemax)
ch=""
for i in range(len(a)):
    if i>=p and i<(p+taillemax):
        ch+="1 "
    else:
        ch+=str(a[i])+" "
stdout.write(ch)

