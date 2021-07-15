n=int(input())
dict1={}
arr=[]
spr=[]
for i in range(2*n-2):
    s=str(input())
    try:
        dict1[s]+=1
    except:
        KeyError
        dict1[s]=1
    arr.append(s)
    if(len(s)==n-1):
        spr.append(s)
flag=0
temp=""
arr1=[0]*(2*n-2)
for i in range(n-1):
    temp+=spr[0][i]
    tempflag=0
    for j in range(2*n-2):
        if(arr[j]==temp and arr1[j]==0):
            arr1[j]=1
            tempflag=1
            break
    if(tempflag==0):
        flag=1
        break
    #print(*arr1)
if(flag==0):
    temp=''
    for i in range(n-2,-1,-1):
        temp=spr[1][i]+temp
        tempflag=0
        for j in range(2*n-2):
            if(arr[j]==temp and arr1[j]==0):
                arr1[j]=-1
                tempflag=1
                break
        if(tempflag==0):
            flag=1
            break
if(flag==0):
    s1=""
    for i in arr1:
        if(i==1):
            s1+='P'
        elif(i==-1):
            s1+='S'
    print(s1)

else:
    temp=""
    arr1=[0]*(2*n-2)
    for i in range(n-1):
        temp+=spr[1][i]
        tempflag=0
        for j in range(2*n-2):
            if(arr[j]==temp and arr1[j]==0):
                arr1[j]=1
                tempflag=1
                break
        if(tempflag==0):
            flag=1
            break
    temp=""
    if(flag==0):
        for i in range(n-2,-1,-1):
            temp=spr[0][i]+temp
            tempflag=0
            for j in range(2*n-2):
                if(arr[j]==temp and arr1[j]==0):
                    arr1[j]=-1
                    tempflag=1
                    break
            if(tempflag==0):
                flag=1
                break
    s1=""
    for i in arr1:
        if(i==1):
            s1+='P'
        else:
            s1+='S'
    print(s1)
#print(*arr1)

