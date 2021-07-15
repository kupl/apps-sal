import sys

input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
data=[0]*(10**5+1)
for i in range(n):
    data[a[i]]+=1

zero,two,four,six,eight=0,0,0,0,0
for i in range(1,10**5+1):
    if data[i]<=1:
        zero+=1
    elif data[i]<=3:
        two+=1
    elif data[i]<=5:
        four+=1
    elif data[i]<=7:
        six+=1
    else:
        eight+=1

for i in range(int(input())):
    t,m=input().split()
    m=int(m)
    if t=="+":
        if data[m]==7:
            eight+=1
            six-=1
        elif data[m]==5:
            six+=1
            four-=1
        elif data[m]==3:
            four+=1
            two-=1
        elif data[m]==1:
            two+=1
        data[m]+=1
    else:
        if data[m]==8:
            eight-=1
            six+=1
        elif data[m]==6:
            six-=1
            four+=1
        elif data[m]==4:
            four-=1
            two+=1
        elif data[m]==2:
            two-=1
        data[m]-=1
    if eight:
        print("YES")
    elif six>=2:
        print("YES")
    elif six==1:
        if four or two:
            print("YES")
        else:
            print("NO")
    elif four>=2:
        print("YES")
    elif four and two>=2:
        print("YES")
    else:
        print("NO")
