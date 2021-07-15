import sys
input = sys.stdin.readline
for f in range(int(input())):
    n=int(input())
    s=input()
    s=s[0:n]
    mn=n
    for i in range(4):
        mins=[n]*4
        mins[i]=0
        if i<2 and s[0]=="L":
            mins[i]=1
        if i>1 and s[0]=="R":
            mins[i]=1
        for j in range(1,n):
            nmins=[n]*4
            nmins[0]=min(mins[2],mins[3])
            nmins[1]=mins[0]
            nmins[2]=mins[3]
            nmins[3]=min(mins[0],mins[1])
            if s[j]=="L":
                nmins[0]+=1
                nmins[1]+=1
            else:
                nmins[2]+=1
                nmins[3]+=1
            for k in range(4):
                mins[k]=nmins[k]
        if i==0:
            mn=min(mn,mins[2],mins[3])
        if i==1:
            mn=min(mn,mins[0])
        if i==2:
            mn=min(mn,mins[3])
        if i==3:
            mn=min(mn,mins[0],mins[1])
    print(mn)

