n=int(input())
lis=input().split()
for i in range(n):
    lis[i]=int(lis[i])
lis2=sorted(lis)
m=int(input())
lis1=[]
for i in range(m):
    lis1.append(input().split())
for i in range(m):
    for j in range(3):
        lis1[i][j]=int(lis1[i][j])

s=[lis[0]]
for i in range(1,n):
    s.append(lis[i]+s[i-1])
s=[0]+s
s2=[lis2[0]]
for i in range(1,n):
    s2.append(lis2[i]+s2[i-1])
s2=[0]+s2

for i in range(m):
    if lis1[i][0]==1:
        print(s[lis1[i][2]]-s[lis1[i][1]-1])
    else:
        print(s2[lis1[i][2]]-s2[lis1[i][1]-1])

