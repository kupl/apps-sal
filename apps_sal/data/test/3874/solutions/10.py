import collections

Input=input().split()
n=int(Input[0])
m=int(Input[1])
listfile=[]

for i in range(n):
    listfile.append(input())

listdet=list(map(int, input().split()))
listfile1=[]

valid = 0
for i in range(len(listdet)):
    if i==0:
        valid = len(listfile[listdet[i]-1])
    elif len(listfile[listdet[i]-1]) != valid:
        valid = -1
        break
    listfile1.append(listfile[listdet[i]-1])

result=''
if valid == -1:
    print("No")
else:
    temp=''
    for i in range(len(listfile1[0])):
        for j in range(len(listfile1)):
            if j==0:
                temp = listfile1[j][i]
            if listfile1[j][i] != temp:
                result+="?"
                break
            elif j == len(listfile1)-1:
                result+= listfile1[j][i]

    count=0
    for i in range(len(listfile)):
        if len(listfile[i]) == len(result) and (i+1 not in listdet):
            for j in range(len(listfile1[0])):
                if listfile[i][j] != result[j] and result[j] != "?":
                    count+=1
                    break
        elif len(listfile[i])!= len(result) and (i+1 not in listdet):
            count+=1
    
    if count == n-m:
        if result == "?"*len(listfile1):
            print("No")
        else:
            print("Yes")
            print(result)
    else:
        print("No")

