n=int(input())
v=list(map(int,input().split()))
numg=[]
numk=[]
for i in range(n):
    if i%2==0:
        numk.append(v[i])
    else:
        numg.append(v[i])
numk.sort()
numg.sort()
numk2=[]
numg2=[]
num1=0
cnt=0
for i in range(len(numk)):
    if num1!=numk[i]:
        numk2.append([num1,cnt])
        num1=numk[i]
        cnt=1
    else:
        cnt+=1
numk2.append([num1,cnt])
num1=0
cnt=0
for i in range(len(numg)):
    if num1!=numg[i]:
        numg2.append([num1,cnt])
        num1=numg[i]
        cnt=1
    else:
        cnt+=1
numg2.append([num1,cnt])
str1= lambda val: val[1]
numg2.sort(key=str1)
numk2.sort(key=str1)
if numg2[-1][0]==numk2[-1][0]:
    print((n-max(numg2[-1][1]+numk2[-2][1],numg2[-2][1]+numk2[-1][1])))
else:
    print((n-(numg2[-1][1]+numk2[-1][1])))

