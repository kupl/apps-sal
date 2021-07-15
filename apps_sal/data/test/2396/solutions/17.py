n=int(input())
d={}
aaa=[]
for ii in range(n):
    s=input().strip()
    arr=list(s)
    for i in range(len(arr)):
        if arr[i] is "(" or arr[i] is "+" or arr[i] is ")" or arr[i] is "/":
            if arr[i] is "/":
                arr[i]=""
            else:
                arr[i]=" "
    a,b,c=map(int,("".join(arr)).split())
    ans=(a+b)/c 
    if ans in d.keys():
        d[ans][0]+=1
        d[ans][1].append(ii)
    else:
        d[ans]=[1,[ii]]
    aaa.append(ans)
arr1={}
for i in d.keys():
    for j in d[i][1]:
        arr1[j]=d[i][0]
for i in range(n):
    print(arr1[i],end=" ")
print("")
        
    
